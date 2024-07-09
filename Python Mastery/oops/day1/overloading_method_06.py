class Math:
    def add(self,a,b,c=None):
        if c:
            return a + b + c 
        else:
            return a + b 

math = Math()
print(math.add(2, 3))     
print(math.add(2, 3, 4))