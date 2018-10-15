class Car(object):

	def __init__(self, model, year, max_speed, type=''):
		self.model = model
		self.year = year
		self.max_speed = max_speed
		self.type = type.capitalize()

	def get_car_type(self):
		return self.type

	def change_type(self, new_type):
		self.type = new_type.capitalize()


class CarGas(Car):

	def __init__(self, model, year, max_speed, type='Gas'):
		super(CarGas, self).__init__(model, year, max_speed)
		self.type = type


class CarPetrol(Car):

	def __init__(self, model, year, max_speed, type='Petrol'):
		super(CarPetrol, self).__init__(model, year, max_speed)
		self.type = type


class CarElectro(Car):

	def __init__(self, model, year, max_speed, type='Electro'):
		super(CarElectro, self).__init__(model, year, max_speed)
		self.type = type


car_bmw = Car('BMW', 2018, 280, 'gas')

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
