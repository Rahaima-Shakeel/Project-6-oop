# Employee class shows access behavior of public, protected, and private variables.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

emp = Employee("Sara", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)
# print(emp.__ssn)  # This will raise an error
print(emp._Employee__ssn)  # Accessing private variable using name mangling