# Rust PyO3 Bazel Example

A minimal example demonstrating how to:
- Build Rust code as a Python extension using [pyo3](https://pyo3.rs/)
- Package it with [Bazel](https://bazel.build) 
- Set up logging between Rust and Python

## Important Files

- `MODULE.bazel`: Defines project dependencies and Rust crate specifications
- `extensions/pyo3_rules.bzl`: Rules for building a rust binary and wrapping it inside a python library
- `rust_lib/`: Contains Rust source code and BUILD file
- `python_lib`: Contains Python source code and BUILD file for importing the Rust module


## Remarks and Limitations

- Can currently only export one python module per rust library (cause we use __init__() for loading them one at a time)
- Python import path is relative to MODULE.bazel
- Current setup is without cargo (as we want to manage dependencies with Bazel), but this can be changed (e.g. with crateuniverse)