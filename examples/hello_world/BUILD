load("//extensions:pyo3_rules.bzl", "pyo3_library")
load("@rules_python//python:defs.bzl", "py_binary")

pyo3_library(
    name = "rust_module",
    module_name = "RustModule",
    srcs = ["lib.rs"],
    deps = [
        "@crates//:pyo3",
        "@crates//:log",
        "@crates//:pyo3-log",
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [":rust_module"]
)