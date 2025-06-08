"""
A module containing Person and Student classes.
"""
# This File is only for the python analyser! Functionality is implemented in Rust.

class Person:
    """
    Represents a person with a name and age.
    Provides functionality to check if the person is an adult.
    """
    name: str # name of the person
    age: int # age of the person

    def __init__(self, name: str, age: int) -> None: 
        """
        :param name: name of the person
        :type name: str
        :param age: age of the person
        :type age: int
        """

    @property
    def is_adult(self) -> bool: 
        """
        Checks if the person is an adult.
        :return: True if the person is an adult, False otherwise
        :rtype: bool
        """

class Student(Person):
    """
    Represents a student, inheriting from Person.
    Adds grade tracking functionality.
    """
    grade: list[int] # grades of the student

    def __init__(self, name: str, age: int) -> None: 
        """
        :param name: name of the student
        """

    def grade_exam(self, bias: float) -> bool:
        """
        Grades the student's exam.
        :param bias: bias of the exam
        :type bias: float
        :return: True if the student passed the exam, False otherwise
        :rtype: bool
        """

    @property
    def grade_average(self) -> float:
        """
        Calculates the student's grade average.
        :return: the student's grade average
        :rtype: float
        """

raise ImportError("This file is only for the python analyser! Functionality is implemented in Rust.") from None
