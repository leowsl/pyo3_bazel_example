load("//extensions:pyo3_rules.bzl", "pyo3_library")

pyo3_library(
    name = "rust_module",
    srcs = ["src/lib.rs"],
    deps = [
        "@crates//:pyo3",
        "@crates//:log",
        "@crates//:pyo3-log",
    ],
    module_name = "RustModule",
    visibility = ["//visibility:public"],
)