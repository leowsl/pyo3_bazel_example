use pyo3::prelude::*;
use log;
use std::time::Instant;

mod benchmark;
mod progress;
mod result;

use result::Result;
use progress::ProgressIndicator;

const THREAD_COUNT: u64 = 8;

#[pyfunction]
fn run_test(iterations: u64, thread_count: u64) -> Result {
    // Run multi-threaded test
    let mut progress = ProgressIndicator::new("Multi-threaded");
    let start = Instant::now();
    let result_multi_thread = benchmark::work_threaded(iterations, thread_count);
    let score_multi_thread = start.elapsed().as_secs_f64();
    progress.stop(score_multi_thread);

    // Run single-threaded test
    let mut progress = ProgressIndicator::new("Single-threaded test");
    let start = Instant::now();
    let result_single_thread = benchmark::work_no_threading(iterations);
    let score_single_thread = start.elapsed().as_secs_f64();
    progress.stop(score_single_thread);

    Result {
        iterations,
        score_single_thread,
        score_multi_thread,
        result_single_thread,
        result_multi_thread,
    }
}

#[pymodule(name = "MultithreadingBenchmark")]
fn multithreading_benchmark(m: &Bound<'_, PyModule>) -> PyResult<()> {
    pyo3_log::init();
    m.add_function(wrap_pyfunction!(run_test, m)?)?;
    m.add_class::<Result>()?;
    Ok(())
}

