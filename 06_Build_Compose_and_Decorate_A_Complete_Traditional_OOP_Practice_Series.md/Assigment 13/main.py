class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine method

# Create an Engine object
my_engine = Engine()

# Pass it to the Car
my_car = Car(my_engine)

# Call the method of Engine via Car
print(my_car.start_car())  # Output: Engine started.
