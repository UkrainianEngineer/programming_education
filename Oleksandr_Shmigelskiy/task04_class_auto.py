class Car(object):
	def __init__(self, type, model, year, max_speed):
		self.type = type
		self.model = model
		self.year = year
		self.max_speed = max_speed

	def get_car_type(self):
		return self.type.capitalize()

	def change_type(self, new_type):
		self.type = new_type.capitalize()


car_bmw = Car('gas', 'BMW', 2018, 280)

print(car_bmw.get_car_type())
car_bmw.change_type('petrol')
print(car_bmw.get_car_type())
