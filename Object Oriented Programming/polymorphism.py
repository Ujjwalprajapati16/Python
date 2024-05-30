class Car:
    def __init__(self, brand, model):
        self.__brand = brand # __ (underscore) used to make variable private
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
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

print(my_car.fuel_type())
print(my_tesla.fuel_type())