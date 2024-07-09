# Single inheritance mean a child class inherits from one parent class
class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    

mack = Dog('Mack')
print(mack.speak())