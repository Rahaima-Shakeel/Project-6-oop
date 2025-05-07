# A custom exception is raised if age is below 18 and caught using try-except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Age is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)