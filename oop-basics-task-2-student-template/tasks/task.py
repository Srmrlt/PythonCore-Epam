# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        person_info = f'Name: {self.name}, Age: {self.age}, '
        return person_info


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        person_info = super().show()
        person_info += f'Salary: {self.salary}'
        return person_info


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        person_info = super().show()
        person_info += f'Grades: {self.grades}'
        return person_info
