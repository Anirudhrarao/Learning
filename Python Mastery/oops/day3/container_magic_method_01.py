class CustomList:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self,index,value):
        self.items[index] = value 
    
    def __delitem__(self,index):
        del self.items[index]
    
    def __repr__(self):
        return f"CustomList({self.items})"

my_list = CustomList()
my_list.items = [1,2,3,4,5]

print(len(my_list))
print(my_list[2])
my_list.items[2] = 3.5
del my_list.items[2]
print(my_list) 