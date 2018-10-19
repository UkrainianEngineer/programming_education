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



 5. Improve previous task to make it possible to run code in this way:

car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
petrol_car.get_model()  # Returns `BMW`
petrol_car.get_year()  # Returns 2018
petrol_car.get_max_speed()  # Returns 300

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.


"""


class Car:
    """Base class for autos."""
    def __init__(self, car_type, model, year, max_speed):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def change_type(self, car_type):
        # Changes only car_type parameter without class changing.
        self.car_type = car_type

    def set_car_type(self, car_type):
        # Changes class of object Car.
        self.__class__ = gett
        self.car_type = car_type
        return self.car_type.title()

    def get_car_type(self):
        return self.car_type.title()

    def get_model(self):
        return self.car_type.title()

    def get_year(self):
        return self.car_type.title()

    def get_max_speed(self):
        return self.car_type.title()

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
car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())

# Change type of object 'Car'
car.change_type('petrol')
print(car.get_car_type())


car = Car('BMW', 2018, 300)
petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
print(car.__class__)
print(petrol_car.__class__)
petrol_car.get_model()  # Returns `BMW`
petrol_car.get_year()  # Returns 2018
petrol_car.get_max_speed()  # Returns 300