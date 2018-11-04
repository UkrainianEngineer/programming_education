class Shape(object):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


shape = Shape()
print(shape.area())  # prints '0'

square = Square(3)
print(square.area())  # prints '9'