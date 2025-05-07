# MathUtils provides a static method to add two numbers without using instance or class data.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))