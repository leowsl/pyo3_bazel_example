load("@rules_python//python:py_binary.bzl", "py_binary")

py_binary(
    name = "main",
    srcs = ["main.py"],
    data = ["//rust_lib:rust_lib_so"]
)
    