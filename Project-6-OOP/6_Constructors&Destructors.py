# Logger prints messages when created and destroyed, demonstrating constructor and destructor.

class Logger:
    def __init__(self):
        print("Logger started.")

    def __del__(self):
        print("Logger stopped.")

l = Logger()
del l