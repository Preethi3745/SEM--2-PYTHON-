from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


w = int(input("Enter the width of the rectangle: "))
h = int(input("Enter the height of the rectangle: "))


r = Rectangle(w, h)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
