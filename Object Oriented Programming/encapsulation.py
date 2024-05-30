class Car:
    def __init__(self, brand, model):
        self.__brand = brand # __ (underscore) used to make variable private
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.model
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterry_size):
        super().__init__(brand, model)
        self.batterry_size = batterry_size
        
    def get_batterry_size(self):
        return self.batterry_size
    

my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())