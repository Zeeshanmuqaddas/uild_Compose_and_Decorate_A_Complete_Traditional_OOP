class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Create an instance of Multiplier with a factor of 5
times_five = Multiplier(5)

# Test if the object is callable
print(callable(times_five))  # Output: True

# Call the object like a function
result = times_five(10)
print(result)  # Output: 50
