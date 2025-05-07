# A class decorator adds a greet() method to the decorated class.

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())