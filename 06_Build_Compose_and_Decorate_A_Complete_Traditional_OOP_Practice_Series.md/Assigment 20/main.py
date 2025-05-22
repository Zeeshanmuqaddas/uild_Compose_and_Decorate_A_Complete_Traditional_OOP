# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print(f"Age {age} is valid.")

# Example usage
try:
    check_age(18)
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")
