class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Example usage:
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # Output: Buddy says: Woof!
