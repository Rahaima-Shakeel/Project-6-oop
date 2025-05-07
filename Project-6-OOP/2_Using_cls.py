# Counter class uses cls to track how many instances have been created.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Objects created: {cls.count}")

a = Counter()
b = Counter()
Counter.show_count()