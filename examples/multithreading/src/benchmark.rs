use std::thread;
use pyo3::prelude::pyfunction;

#[pyfunction]
pub fn work(start: u64, end: u64) -> f64 {
    let mut sum = 0.0;
    for i in start..end {
        sum += (i as f64).sqrt().sin();
    }
    sum
}

pub fn work_no_threading(iterations: u64) -> f64 {
    work(0, iterations)
}

pub fn work_threaded(iterations: u64, thread_count: u64) -> f64 {
    // Distribute the work
    let chunk_size = iterations / thread_count;
    let mut work_assignments: Vec<(u64, u64)> = Vec::new();
    for i in 0..(thread_count-1) {
        work_assignments.push((i * chunk_size, (i + 1) * chunk_size));
    }
    work_assignments.push(((thread_count - 1)  * chunk_size, iterations));

    let mut handles = vec![];
    for (start, end) in work_assignments {
        handles.push(thread::spawn(move || {
            work(start, end)
        }));
    }

    // Collect the results
    let mut sum = 0.0;
    for handle in handles {
        sum += handle.join().unwrap();
    }
    sum
}