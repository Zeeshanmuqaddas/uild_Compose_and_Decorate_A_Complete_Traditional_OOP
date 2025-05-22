class Student:
    def __init__(self, name, marks):
        self.name = name        # Initialize name
        self.marks = marks      # Initialize marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Zeeshan", 85)
student1.display()
