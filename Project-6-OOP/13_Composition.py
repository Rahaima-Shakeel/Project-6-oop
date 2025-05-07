# Car class has an Engine object and calls its start() method to demonstrate composition.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start()