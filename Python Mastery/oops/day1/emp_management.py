class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    
    def get_details(self):
        return f"{super().get_details()} Department: {self.department}"
    
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def get_details(self):
        return f"{super().get_details()} Programming Language: {self.programming_language}"

# Creating instances of Manager and Developer
manager = Manager("Alice", 90000, "HR")
developer = Developer("Bob", 80000, "Python")

print(manager.get_details())   
print(developer.get_details()) 