from examples.classes.RustClasses import Person, Student

person = Person("John", 20)
if person.is_adult:
    print(f"John is {'an' if person.is_adult else 'not an'} adult")

student = Student("Jane", 20)
for i in range(10):
    passed_exams = student.grade_exam(bias = 1.2)

print(f"Jane {'passed' if student.grade_average <= 4 else 'failed'} the exams with a grade average of {student.grade_average}")
print(f"Grades: {student.grades}")