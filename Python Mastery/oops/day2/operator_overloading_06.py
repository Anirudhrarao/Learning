# Python allows you to change behaviour for standard operator like add sub mul div
class Vector:
    def __init__(self, x, y):
        self.x = x  
        self.y = y 
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2,3)
v2 = Vector(3,2)
result = v1 + v2 
print(result)