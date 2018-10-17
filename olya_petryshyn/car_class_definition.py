class Car(object):
    """
    This class represents Car.
    """
    def __init__(self, car_type, model, year, max_speed):
        """
        The constructor for Car class.
        :param car_type: Type of particular car.
        :param model: Model of car.
        :param year: Year of production.
        :param max_speed: Max speed the car is able to reach.
        """
        self.car_type = car_type
        self.model = model
        self.year = year
        self.max_speed = max_speed
        
    def get_car_type(self):
        """
        Class method, which returns type of the car.
        :return: The type of the car.
        """
        return self.car_type
        
    def change_type(self, new_car_type):
        """
        Class method, that changes type of the car.
        :param new_car_type: New type of the car.
        """
        self.car_type = new_car_type
        

class ElectricCar(Car):
    """
    This class represents Electro Car, inherited for class Car.
    """
    car_type = "electric"
    
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    
class GasCar(Car):
    """
    This class represents Gas Car, inherited for class Car.
    """
    car_type = "gas"
    
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    
class PetrolCar(Car):
    """
    This class represents Petrol Car, inherited for class Car.
    """
    car_type = "petrol"
    
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    
car = Car('gas', 'BMW', 2018, 280)
print(car.get_car_type())  # prints 'Gas'
car.change_type('petrol')
print(car.get_car_type())  # prints 'Petrol'
electro_car = ElectricCar('Tesla Model X', 2015, 250)
print(electro_car.get_car_type())   # prints 'Electric'
