use pyo3::prelude::*;
use log;

#[pyfunction]
pub fn hello_world() -> PyResult<()> {
    log::info!("Hello World!");
    return PyResult::Ok(())
}

#[pymodule(name = "RustModule")]
pub fn rust_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    pyo3_log::init();
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    return PyResult::Ok(())
}