use pyo3::prelude::*;

use log;
use env_logger;

#[pyfunction]
pub fn hello_world() -> PyResult<()> {
    env_logger::init();
    log::info!("Hello World from lib!");
    return PyResult::Ok(())
}

#[pymodule]
pub fn rust_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    return PyResult::Ok(())
}