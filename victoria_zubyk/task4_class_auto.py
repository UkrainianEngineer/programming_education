class Auto:
    def __init__(self,type , model,year,max_speed ):
        self.type = type
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def get_car_type(self):
        return self.type

    def change_type(self, new_type):
        if (new_type != self.type):
            self.type = new_type

class GasAuto(Auto):
    def __init__(self, model, year, max_speed):
        super().__init__(type, model, year, max_speed)

    def get_car_type(self):
        print('gas')

class ElectroAuto(Auto):
    def __init__(self, model, year, max_speed):
        super().__init__(type, model, year, max_speed)

    def get_car_type(self):
        print('electro')

class PetrolAuto(Auto):
    def __init__(self, model, year, max_speed):
        super().__init__(type, model, year, max_speed)

    def get_car_type(self):
        print('petrol')

car = Auto('gas', 'BMW', 2018, 280)
print(car.get_car_type())
car.change_type('petrol')
print(car.get_car_type())
