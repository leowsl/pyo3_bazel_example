use pyo3::prelude::*;
use rand::Rng;

#[pyclass(subclass)]
#[derive(Debug, Clone)]
pub struct Person {
    #[pyo3(get)]
    pub name: String,
    #[pyo3(get, set)]
    pub age: u32,
}

#[pymethods]
impl Person {
    #[new]
    pub fn new(name: String, age: u32) -> Self {
        Self { name, age }
    }

    #[getter]
    pub fn is_adult(&self) -> PyResult<bool> {
        Ok(self.age >= 18)
    }
}

#[pyclass(extends=Person, subclass)]
#[derive(Debug, Clone)]
pub struct Student {
    #[pyo3(get, set)]
    pub grades: Vec<u32>,
}

#[pymethods]
impl Student {
    #[new]
    pub fn new(name: String, age: u32) -> (Self, Person) {
        (Self { grades: vec![] }, Person::new(name, age))
    }

    pub fn grade_exam(&mut self, bias: f32) -> PyResult<bool> {
        let mut rng = rand::rng();
        let mut grade = rng.random_range(0..100) as f32 * bias;
        grade = grade.clamp(0.0, 100.0);
        let grade = 1.0 + (grade / 100.0) * 5.0;
        let grade = grade.round() as u32;
        
        self.grades.push(grade);
        Ok(grade <= 4)
    }

    #[getter]
    pub fn grade_average(&self) -> PyResult<f32> {
        let sum: u32 = self.grades.iter().sum();
        let average = sum as f32 / self.grades.len() as f32;
        Ok(average)
    }
}