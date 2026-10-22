class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, s):
        self.students.append(s)

t = Teacher("Mr. Lee")
t.add_student(Student("Zoe"))
print(t.students[0].name)