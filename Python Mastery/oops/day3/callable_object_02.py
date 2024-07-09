class Adder:
    def __init__(self,value):
        self.value = value
    
    def __call__(self,x):
        return self.value + x

# create object for adder class
add = Adder(10)

print(add(20))