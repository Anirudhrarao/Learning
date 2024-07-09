from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self,height, width):
        self.height = height 
        self.width = width
    def area(self):
        return self.height * self.width

rect = Rectangle(10,20)
area = rect.area()
print(f'Area of rectangle is {area}')