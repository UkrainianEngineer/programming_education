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

import sys, inspect


class Car:
    """Base class for autos."""
    car_type = 'Car'
    def __init__(self, model, year, max_speed, car_type="Car"):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def change_type(self, car_type):
        # Changes only car_type parameter without class changing.
        self.car_type = car_type

    def set_car_type(self, new_type):
        # Changes class of object Car.
        found_class = False
        for key, data in inspect.getmembers(sys.modules[__name__], inspect.isclass):
            if data.car_type == new_type.title():
                setattr(self, '__class__', getattr(sys.modules[__name__], data.__name__, Car))
                self.car_type = new_type
                found_class = True
        if not found_class:
            self.__class__ = Car
            print('Class for new car type not found. Base class set.')

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
    car_type = 'Gas'

    def __init__(self):
        super().__init__()
        self.car_type = self.__class__.car_type


class ElectroCar(Car):
    """Electro car class."""
    car_type = 'Electro'

    def __init__(self):
        super().__init__()
        self.car_type = self.__class__.car_type


class PetrolCar(Car):
    """Petrol car class."""
    car_type = 'Petrol'

    def __init__(self):
        super().__init__()
        self.car_type = self.__class__.car_type


if __name__ == '__main__':
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
    petrol_car = car.set_car_type('petroewhgtl')  # It returns Car instance.
    print(petrol_car)
    petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
    print(petrol_car)
    print(petrol_car.get_model())  # Returns `BMW`
    print(petrol_car.get_year())  # Returns 2018
    print(petrol_car.get_max_speed())  # Returns 300
    print(petrol_car.get_car_type())  # Returns Petrol
    gas_car = car.set_car_type('gas')  # It returns `GasCar` instance
    print(gas_car)
    print(gas_car.get_car_type())  # Returns Petrol
    print(petrol_car)
    print(car)
