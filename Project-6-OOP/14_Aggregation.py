# Department holds a reference to an existing Employee, showing loose coupling (aggregation).

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Ayesha")
dept = Department(emp)
print(dept.employee.name)