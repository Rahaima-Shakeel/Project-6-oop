# Teacher class uses super() to initialize name from Person class, then adds subject.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("John", "Math")
print(t.name, t.subject)