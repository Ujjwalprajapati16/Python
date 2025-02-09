class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self._age}, Gender: {self.__gender}.")
        
    def getGender(self):
        return self.__gender
    
    
s1 = Student("Pikachu", 18, 'M')
s1.display()