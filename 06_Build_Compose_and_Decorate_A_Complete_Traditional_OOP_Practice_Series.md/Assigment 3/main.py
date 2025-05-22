# Define the Car class
class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start(self):
        print(f"{self.brand} car is starting...")

# Instantiate the class
my_car = Car()

# Access the public variable
print("Brand:", my_car.brand)

# Call the public method
my_car.start()
