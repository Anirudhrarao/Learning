# Mutliple inheritanc mean a child class inherits from two or more than multiple parent class
class Canine:
    def canine_method(self):
        return "This is a canine."

class Pet:
    def pet_method(self):
        return "This is a pet."

class Dog(Canine, Pet):
    def __init__(self,name):
        self.name = name 
    
    def pet_method(self):
        return f"{self.name} is pet"

mack = Dog('Mack')
print(mack.pet_method())
print(mack.canine_method())
