""" Script defines a class named `Shape` and its subclass `Square`.

The `Square` class has an init function which takes a length as
argument.
Both classes have a `area` function which can print the area of the
shape where `Shape`'s area is 0 by default.

It might be used like this:
square = Square(3)
print(square.area())
"""


class Shape:
    def __init__(self, length=0):
        self.length = length

    def area(self):
        # We don`t know what is it the shape, so area is 0.
        print("The type of the shape is unknown.")
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


square = Square(3)
print(square.area())

shape = Shape(4)
shape1 = Shape()
print(shape.area())
print(shape.length)
print(shape1.area())
print(shape1.length)


