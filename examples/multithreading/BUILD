load("//extensions:pyo3_rules.bzl", "pyo3_library")
load("@rules_python//python:defs.bzl", "py_binary")

pyo3_library(
    name = "multithreading",
    module_name = "MultithreadingBenchmark",
    srcs = [
        "src/lib.rs",
        "src/benchmark.rs",
        "src/progress.rs",
        "src/result.rs",
    ],
    deps = [
        "@crates//:pyo3",
        "@crates//:log",
        "@crates//:pyo3-log",
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py", "benchmark.py"],
    deps = [":multithreading"],
)