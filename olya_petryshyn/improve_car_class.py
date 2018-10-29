class Car(object):
    def __init__(self, model, year, max_speed, car_type='NULL'):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.car_type = car_type

    def get_car_type(self):
        return self.car_type

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_max_speed(self):
        return self.max_speed

    def change_type(self, new_car_type):
        self.car_type = new_car_type

    def set_car_type(self, some_car_type):
        for child_class in Car.__subclasses__():
            temp_object = child_class(self.model, self.year, self.max_speed)
            if some_car_type.title() == temp_object.car_type:
                self = temp_object
                return self


class ElectricCar(Car):
    car_type = "electric"

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed


class GasCar(Car):
    car_type = "gas"

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed


class PetrolCar(Car):
    car_type = "petrol"

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

car = Car('BMW', 2018, 280)
car.change_type('petrol')
print(car.get_car_type())   # prints 'petrol'
petrol_car = car.set_car_type('petrol')