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
    
class Battery:
    def battery_info(self):
        return "This car has a 12v battery"

class Engine:
    def engine_info(self):
        return "This car has a 2.0L engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass
    
my_car = Car("Toyota", "Corolla")
my_tesla  = ElectricCar("Tesla", "Model S", "85kwh")
safari = Car("Tata", "Naxon")

my_new_tesla = ElectricCarTwo("Tesla", "Model2")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())