load("@rules_rust//rust:defs.bzl", "rust_shared_library")
load("@rules_rust//rust:defs.bzl", "rust_binary")
load("@crates//:defs.bzl", "all_crate_deps")

rust_shared_library(
    name = "rust_module_lib",
    srcs = ["src/lib.rs"],
    deps = all_crate_deps(),
    visibility = ["//visibility:private"],
)

genrule(
    name = "rust_module",
    srcs = [":rust_module_lib"],
    outs = ["rust_module.so"],
    visibility = ["//visibility:public"],
    cmd = "cp $< $@",
)   
