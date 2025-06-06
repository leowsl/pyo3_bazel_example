load("@rules_rust//rust:defs.bzl", "rust_library")
load("@rules_rust//rust:defs.bzl", "rust_binary")
load("@rules_rust//rust:defs.bzl", "rust_binary")
load("@crates//:defs.bzl", "all_crate_deps")

package(default_visibility = ["//visibility:public"])

rust_library(
    name = "rust_lib",
    srcs = ["src/lib.rs"],
    deps = all_crate_deps(normal = True)
)

rust_binary(
    name = "rust_lib_main",
    srcs = ["src/main.rs"],
    deps = ["//rust_lib"],
)
