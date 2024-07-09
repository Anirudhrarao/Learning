# Multilevel mean a child class inherits from parent class and parent class inherits from grandfather of child class.

class Animal:
    def __init__(self,name):
        self.name = name 
    
class Mammals(Animal):
    def __init__(self,name,has_fur):
        super().__init__(name)
        self.has_fur = has_fur 
    
class Dog(Mammals):
    def __init__(self,name,has_fur,breed):
        super().__init__(name,has_fur)
        self.breed = breed 

    def description(self):
        return f"{self.name} is a {self.breed} with {'fur' if self.has_fur else 'no fur'}."

my_dog = Dog("Buddy", False, "Golden Retriever")
print(my_dog.description())