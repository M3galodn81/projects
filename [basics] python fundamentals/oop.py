# Object - Oriented Programming

class Student:
    def __init__(self,name,section):
        self.name = name
        self.section = section

    def __str__(self):
        return f"{self.name}({self.section})"

student = Student('John','STEM D')
print(student)

class Person(Student):
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def __str__(self):
        return f'{self.name} is a {self.job}'

print(Person('Hans','Teacher'))
