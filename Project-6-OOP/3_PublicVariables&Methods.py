# Car class has public brand and start() method accessible from outside.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

c = Car("Toyota")
print(c.brand)
c.start()