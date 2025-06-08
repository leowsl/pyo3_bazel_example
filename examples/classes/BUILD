load("//extensions:pyo3_rules.bzl", "pyo3_library")
load("@rules_python//python:defs.bzl", "py_binary")

pyo3_library(
    name = "pyo3_module",
    module_name = "RustClasses",
    srcs = glob(["src/**/*.rs"]),
    deps = [
        "@crates//:pyo3",
        "@crates//:rand",
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [":pyo3_module"]
)