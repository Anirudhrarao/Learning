# Hierarchical inheritance means a more than two child class inherits from one parent class
class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return  f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return  f"{self.name} says Meow!"

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
print(my_dog.speak())  
print(my_cat.speak())