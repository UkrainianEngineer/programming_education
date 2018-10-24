class Car(object):

    def __init__(self, model, year, max_speed, car_type='Not defined'):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.car_type = car_type

    def get_car_type(self):
        return self.car_type.title()

    def change_type(self, new_type):
        self.car_type = new_type

    def set_car_type(self, car_type):
        # return CarPetrol(self.model, self.year, self.max_speed)
        self.__class__ = CarPetrol
        return self

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed


class CarGas(Car):

    def __init__(self, model, year, max_speed):
        super(CarGas, self).__init__(model, year, max_speed)
        self.car_type = 'Gas'


class CarPetrol(Car):

    def __init__(self, model, year, max_speed):
        super(CarPetrol, self).__init__(model, year, max_speed)
        self.car_type = 'Petrol'


class CarElectro(Car):

    def __init__(self, model, year, max_speed):
        super(CarElectro, self).__init__(model, year, max_speed)
        self.car_type = 'Electro'


car = Car('BMW', 2018, 300)

petrol_car = car.set_car_type('petrol')  # It returns `PetrolCar` instance.
print(petrol_car.get_model())  # Returns `BMW`
print(petrol_car.get_year())  # Returns 2018
print(petrol_car.get_max_speed())  # Returns 300
print(petrol_car.get_car_type())
print(petrol_car.__class__)
car.__class__ = CarPetrol
print(car.__class__)

gas_car = car.set_car_type('gas')  # It returns `GasCar` instance.
