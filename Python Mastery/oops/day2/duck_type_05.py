class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def play_sound(animal: Animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()

print(play_sound(dog))  # Output: Woof!
print(play_sound(cat))  # Output: Meow!
