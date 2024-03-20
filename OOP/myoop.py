class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Car(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"


# Creating instances of Car and Motorcycle
my_car = Car("Toyota", "Camry", 2020)

# Using the start and stop methods without needing to know the internal implementation
print(my_car.start())
print(my_car.stop())




# Code Explained
# __init__: special METHOD in Python classes known as a CONSTRUCTOR. It is automatically called when an instance of the class is created.
# self: This parameter refers to instance of the class itself. It allows the instance to access its own attributes and methods.
# return - used to exit a function and return a value to the caller.