# A Student class uses self to store and display name and marks of a student.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Ali", 85)
s1.display()