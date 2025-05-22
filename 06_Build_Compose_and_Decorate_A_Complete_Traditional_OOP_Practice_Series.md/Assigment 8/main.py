class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor to set name
        self.subject = subject

# Example usage:
t = Teacher("Alice", "Math")
print(t.name)     # Output: Alice
print(t.subject)  # Output: Math
