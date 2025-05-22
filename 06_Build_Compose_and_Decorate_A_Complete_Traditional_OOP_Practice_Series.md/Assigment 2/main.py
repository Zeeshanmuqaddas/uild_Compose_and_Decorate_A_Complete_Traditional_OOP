class Counter:
    # Class variable to keep track of the number of objects
    count = 0

    def __init__(self):
        # Increment the class variable when a new object is created
        Counter.count += 1

    @classmethod
    def get_count(cls):
        # Class method to return the current count
        return cls.count


# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print("Number of Counter objects created:", Counter.get_count())  # Output: 3
