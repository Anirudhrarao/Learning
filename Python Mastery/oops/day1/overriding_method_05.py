class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog says woof!"
    
my_dog = Dog()
print(my_dog.speak())

# Method overriding means change implementation but name of method remail will same.