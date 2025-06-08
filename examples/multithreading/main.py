from examples.multithreading.MultithreadingBenchmark import run_test
from examples.multithreading.benchmark import work_threaded, work_no_threading

TEST_BENCH = [1_000, 1_000_000, 100_000_000, 200_000_000, 500_000_000]

print("Running benchmarks...")
print("=" * 60)

for test in TEST_BENCH:
    print(f"\nTest size: {test:,}")
    print("-" * 40)

    # Run Rust
    result = run_test(test, 8)

    # Run Python
    py_single_time, py_single_result = work_no_threading(test)
    py_multi_time, py_multi_result = work_threaded(test, 8)

    # Calculate speedups
    rust_speedup = result.score_single_thread / result.score_multi_thread
    py_speedup = py_single_time / py_multi_time
    total_speedup = py_single_time / result.score_multi_thread

    # Print results
    print(f"Rust:   {result.score_single_thread:.3f}s / {result.score_multi_thread:.3f}s")
    print(f"Python: {py_single_time:.3f}s / {py_multi_time:.3f}s")
    print(f"Speedups:")
    print(f"  Rust:   {rust_speedup:.1f}x")
    print(f"  Python: {py_speedup:.1f}x")
    print(f"  Total:  {total_speedup:.1f}x")
    print(f"Results match:")
    print(f"  Rust: {'✓' if result.correct else '✗'}")
    print(f"  Single thread: {'✓' if abs(result.result_single_thread - py_single_result) < 1e-5 else '✗'}")
    print(f"  Multi thread:  {'✓' if abs(result.result_multi_thread - py_multi_result) < 1e-5 else '✗'}")