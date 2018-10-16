"""4. Define a base class for auto.
Base class should contain:
Fields:
 - type (gas, electro, petrol)
 - model
 - year
 - max speed.
Method:
 - get car type

Define child classes for each type of car.
`get_car_type` method should return just an appropriate type of car.

Create a general class which should work in this way:

car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())  # prints `Gas`
car.change_type('petrol')
print(car.get_car_type())  # prints `Petrol`.
"""


class Car:
    def __init__(self, type, model, year, max_speed):
        self.type = type
        self.model = model
        self.year = year
        self.max_speed = max_speed


    def change_type(self, type):
        self.__class__ = eval(type.title())
        self.type = type

    def get_car_type(self):
        return self.type.title()

class Gas(Car):
    def __init__(self):
        super().__init__()
        self.type = 'Gas'

class Electro(Car):
    def __init__(self):
        super().__init__()
        self.type = 'Electro'

class Petrol(Car):
    def __init__(self):
        super().__init__()
        self.type = 'Petrol'

car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())
car.change_type('petrol')
print(car.get_car_type())
