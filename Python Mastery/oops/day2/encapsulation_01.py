class Employee:

  def __init__(self, name, salary) -> None:
    self.name = name
    self.__salary = salary

  @property
  def salary(self):
    return self.__salary

  @salary.setter
  def salary(self, salary):
    if self.__salary > 0:
      self.__salary = salary
    else:
      return ValueError("Invalid salary")


emp = Employee("John", 5000)
print(emp.name)
print(emp.salary)
emp.salary = 41000

print(emp.salary) 