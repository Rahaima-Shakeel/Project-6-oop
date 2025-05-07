# Multiplier objects can be used like functions to multiply a value by their factor.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiplier(3)
print(callable(m))
print(m(10))