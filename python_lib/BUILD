load("//extensions:pyo3_rules.bzl", "pyo3_library")
load("@rules_python//python:py_binary.bzl", "py_binary")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = ["//rust_lib:rust_module"],
    main = "main.py",
)