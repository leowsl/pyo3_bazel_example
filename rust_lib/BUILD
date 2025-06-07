load("@crates//:defs.bzl", "all_crate_deps")
load("//extensions:pyo3_rules.bzl", "pyo3_library")


pyo3_library(
    name = "rust_module",
    srcs = ["src/lib.rs"],
    deps = all_crate_deps(),
    module_name = "RustModule",
    visibility = ["//visibility:public"],
)