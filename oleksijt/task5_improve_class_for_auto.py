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
 - change car class
 - get car model
 - get car year
 - get car max speed
"""

import sys


class Car:
    """Base class for autos."""
    car_class_types = {
        'Petrol': 'PetrolCar',
        'Gas': 'GasCar',
        'Electro': 'ElectroCar',
        'Car': 'Car'
    }

    def __init__(self, model, year, max_speed, car_type="Car"):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def find_new_car_class(car_type):
        # Find class for new car type.
        found_class = Car.car_class_types.get(car_type)
        if found_class:
            return found_class
        else:
            print('New car type not found. Base class set.')
            return 'Car'

    def change_type(self, car_type):
        # Changes only car_type parameter without class changing.
        self.car_type = car_type

    def set_car_type(self, car_type):
        # Changes class of object Car.
        new_car_class = Car.find_new_car_class(car_type.title())
        self.__class__ = getattr(sys.modules[__name__], new_car_class)
        self.car_type = car_type
        return self

    def get_car_type(self):
        return self.car_type.title()

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed


class GasCar(Car):
    """Gas car class."""
    def __init__(self):
        super().__init__()
        self.car_type = 'Gas'


class ElectroCar(Car):
    """Electro car class."""
    def __init__(self):
        super().__init__()
        self.car_type = 'Electro'


class PetrolCar(Car):
    """Petrol car class."""
    def __init__(self):
        super().__init__()
        self.car_type = 'Petrol'


# Create new object 'Car'
car1 = Car('BMW', 2018, 280, 'gas')
print(car1.get_car_type())

# Change type of object 'Car'
car1.change_type('petrol')
print(car1.get_car_type())

# Create  new object 'Car'
car = Car('BMW', 2018, 300)
print(car)

# Change object class
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
print(petrol_car)
print(petrol_car.get_model())  # Returns `BMW`
print(petrol_car.get_year())  # Returns 2018
print(petrol_car.get_max_speed())  # Returns 300
print(petrol_car.get_car_type())  # Returns Petrol
