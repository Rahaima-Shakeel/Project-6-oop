# Dog class has instance method bark() that prints a message with dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

d = Dog("Buddy", "Labrador")
d.bark()