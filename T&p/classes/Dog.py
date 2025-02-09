class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
dog = Dog("Buddy", 3)
# print(dog.species, dog.name, dog.age)

dog.species = "Lebrradog"
# print(dog.species)

# dog1 = Dog("Dedda", 5)
# print(dog1.name)
# print(dog1.age)
# print(dog1.species)

class lebrradog(dog):
    breed = 'Lebrradog'
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
        
dog2 = lebrradog("Dedda", 5, "Lebrradog")
print(dog2.name)
print(dog2.age)
print(dog2.species)
print(dog2.breed)
