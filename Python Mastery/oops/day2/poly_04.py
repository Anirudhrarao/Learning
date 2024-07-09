class Dog:
    def speak(self):
        return "woof"

class Cat:
    def speak(self):
        return "meow"

def make_sound(animal):
    return animal.speak()

d = Dog()
c = Cat()
print(make_sound(d))
print(make_sound(c))