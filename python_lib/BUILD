load("@rules_python//python:py_binary.bzl", "py_binary")

py_binary(
    name = "main",
    srcs = ["main.py", "importer.py"],
    data = ["//rust_lib:rust_module"],
    main = "main.py",
)
    