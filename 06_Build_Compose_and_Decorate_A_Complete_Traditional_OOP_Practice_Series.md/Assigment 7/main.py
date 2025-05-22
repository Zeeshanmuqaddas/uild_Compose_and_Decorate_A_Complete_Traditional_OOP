class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public variable
        self._salary = salary     # protected variable (by convention)
        self.__ssn = ssn          # private variable (name mangled)


# Create an object of Employee
emp = Employee("John Doe", 50000, "123-45-6789")

# Access public variable
print(emp.name)        # Output: John Doe

# Access protected variable
print(emp._salary)     # Output: 50000  (possible, but discouraged by convention)

# Access private variable
print(emp.__ssn)       # This will cause an AttributeError
