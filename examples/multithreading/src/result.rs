use pyo3::prelude::*;

#[pyclass]
#[derive(Clone)]
pub struct Result {
    #[pyo3(get)]
    pub iterations: u64,
    #[pyo3(get)]
    pub score_single_thread: f64,
    #[pyo3(get)]
    pub score_multi_thread: f64,
    #[pyo3(get)]
    pub result_single_thread: f64,
    #[pyo3(get)]
    pub result_multi_thread: f64,
}

#[pymethods]
impl Result {
    #[getter]
    pub fn correct(&self) -> bool {
        self.result_single_thread > self.result_multi_thread
    }
}
