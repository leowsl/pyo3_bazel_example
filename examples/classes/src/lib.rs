use pyo3::prelude::*;

mod person;

#[pymodule(name = "RustClasses")]
fn classes_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<person::Person>()?;
    m.add_class::<person::Student>()?;
    return PyResult::Ok(())
}
