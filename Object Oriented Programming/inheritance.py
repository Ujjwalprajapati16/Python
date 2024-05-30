class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterry_size):
        super().__init__(brand, model)
        self.batterry_size = batterry_size
        
    def get_batterry_size(self):
        return self.batterry_size
            

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(my_tesla.get_model())
print(my_tesla.get_batterry_size())
print(my_tesla.get_brand())