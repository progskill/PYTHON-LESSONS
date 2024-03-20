# Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Class, Object, Encapsulation
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Encapsulated attribute
    def area(self):
        return 3.14 * self.__radius * self.__radius

# Inheritance

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Class, Object, Encapsulation
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Encapsulated attribute
    def area(self):
        return 3.14 * self.__radius * self.__radius

# Inheritance
class Square(Shape):
    def __init__(self, side):
        self.__side = side  # Encapsulated attribute
    def area(self):
        return self.__side * self.__side

# Polymorphism
def print_area(shape):
    print("Area:", shape.area())

# Create objects and demonstrate polymorphism
circle = Circle(5)
square = Square(4)
print_area(circle)  # Output: Area: 78.5
print_area(square)  # Output: Area: 16