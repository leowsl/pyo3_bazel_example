load("@rules_rust//rust:defs.bzl", "rust_shared_library")
load("@rules_python//python:py_library.bzl", "py_library")
load("@bazel_skylib//rules:copy_file.bzl", "copy_file")

def pyo3_library(
    name,
    srcs,
    deps,
    module_name,
):
    """Creates a python library that uses a pyo3 rust library.
    
    Args:
        name: The name of the target
        srcs: Rust source files
        deps: Rust dependencies
        module_name: The name of the Python module
    """

    rust_shared_library(
        name = name + "_lib",
        srcs = srcs,
        deps = deps,
    )

    # Symlink for shared library
    copy_file(
        name = name + "_so",
        src = name + "_lib",
        out = module_name + ".so",
        allow_symlink = True,
    )

    # Copy module importer to the output directory
    copy_file(
        name = name + "_init",
        src = "//extensions:module_importer.py",
        out = "__init__.py",
        allow_symlink = True,
    )

    py_library(
        name = name,
        srcs = [name + "_init"],
        data = [name + "_so"]
    )
