load("@rules_rust//rust:defs.bzl", "rust_shared_library")
load("@rules_python//python:py_library.bzl", "py_library")
load("@bazel_skylib//rules:copy_file.bzl", "copy_file")

def pyo3_library(
    name,
    srcs,
    deps,
    module_name = "",
    visibility = ["//visibility:public"],
):
    """Creates a PyO3 library that can be imported in Python.
    
    Args:
        name: The name of the target
        srcs: Rust source files
        deps: Rust dependencies
        module_name: The name of the Python module
        visibility: The visibility of the Python library
    """
    rust_shared_library(
        name = name + "_lib",
        srcs = srcs,
        deps = deps,
        visibility = ["//visibility:private"],
    )

    copy_file(
        name = name + "_so",
        src = name + "_lib",
        out = name + ".so",
        allow_symlink = True,
        visibility = ["//visibility:private"],
    )

    # Generate __init__.py with the module loading code
    native.genrule(
        name = name + "_init",
        outs = ["__init__.py"],
        visibility = ["//visibility:private"],
        cmd = """
cat > $@ << 'EOF'
import importlib.util
import sys
import os

def load_so_module(path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Could not find module spec for {module_name}")
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ImportError(f"Module {module_name} has no loader")
    spec.loader.exec_module(module)
    sys.modules[module_name] = module

# Get the path to the .so file
so_path = os.path.join(os.path.dirname(__file__), "{so_file}")
load_so_module(so_path, "{module_name}")
import {module_name}
EOF
        """.format(
            so_file = name + ".so",
            module_name = module_name,
        ),
    )

    py_library(
        name = name,
        srcs = [name + "_init"],
        data = [name + "_so"],
        visibility = visibility,
    )
