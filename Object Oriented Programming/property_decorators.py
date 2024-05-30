class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand # __ (underscore) used to make variable private
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
    
    @property
    def get_model(self):
        return self.__model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are amazing"
    
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterry_size):
        super().__init__(brand, model)
        self.batterry_size = batterry_size
        
    def get_batterry_size(self):
        return self.batterry_size
    
    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Toyota", "Corolla")
my_tesla  = ElectricCar("Tesla", "Model S", "85kwh")
safari = Car("Tata", "Naxon")

print(my_car.get_model)