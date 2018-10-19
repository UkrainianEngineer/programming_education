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


car_bmw = Car('BMW', 2018, 280, 'petrol')

print(car_bmw.get_car_type())
car_bmw.change_type('petrol')
print(car_bmw.get_car_type())


car_ford_gas = CarGas('Ford', 2005, 210)

print(car_ford_gas.get_car_type())
car_ford_gas.change_type('petrol')
print(car_ford_gas.get_car_type())


car_nissan_electro = CarElectro('Nissan', 2016, 190)

print(car_nissan_electro.get_car_type())
car_nissan_electro.change_type('petrol')
print(car_nissan_electro.get_car_type())
