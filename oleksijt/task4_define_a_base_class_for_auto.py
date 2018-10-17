""" This code creates class Car and derived classes for car types.
 Base class contain:
Fields:
 - type (gas, electro, petrol)
 - model
 - year
 - max speed.
Methods:
 - get car type
 - change car type
"""


class Car:
    """ Base class for autos. """
    def __init__(self, car_type, model, year, max_speed):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def change_type(self, car_type):
        """ Change car_type. """
        self.car_type = car_type  # Set new type.

    def get_car_type(self):
        return self.car_type.title()


class Gas(Car):
    """ Gas car class. """
    def __init__(self):
        super().__init__()
        self.car_type = 'Gas'


class Electro(Car):
    """ Electro car class. """
    def __init__(self):
        super().__init__()
        self.car_type = 'Electro'


class Petrol(Car):
    """ Petrol car class. """
    def __init__(self):
        super().__init__()
        self.car_type = 'Petrol'


car = Car('gas', 'BMW', 2018, 280)  # Create new object 'Car'
print(car.get_car_type())
car.change_type('petrol')  # Change type and class of object 'Car'
print(car.get_car_type())
