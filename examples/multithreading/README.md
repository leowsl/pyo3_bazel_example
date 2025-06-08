# Multithreading Benchmark

This example benchmarks Rust vs Python performance, comparing single-threaded and multi-threaded execution.

## Implementation Details

### Implementation Overview
Both implementations perform the same mathematical operation:
```python
sum(sin(sqrt(i)) for i in range(iterations))
```
Both Rust and Python implementations use 8 threads and share identical functionality, with Rust using native threads and PyO3 for Python interop, while Python utilizes ThreadPoolExecutor. The Rust version includes additional features like a progress indicator.

## Sample Results

Here's a sample output from running the benchmark with 1 billion iterations:

```
Test size: 1,000,000,000
----------------------------------------
Rust:   16.470s / 2.094s
Python: 90.482s / 142.070s
Speedups:
  Rust:   7.9x
  Python: 0.6x
  Total:  43.2x
Results match:
  Rust: ✓
  Single thread: ✓
  Multi thread:  ✓
```

## Running the Benchmark

Modify the `TEST_BENCH` to not overload your system.
To run the benchmark:

```bash
bazel run //examples/multithreading:main
```

The benchmark will run with different iteration counts to demonstrate scaling behavior.
