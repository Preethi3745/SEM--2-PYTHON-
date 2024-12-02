class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name=",self.name,"Age=",self.age)
class Employee(Person):
    def __init__(self,name,age,ID):
        super().__init__(name,age)
        self.ID=ID
    def display(self):
        self.show()
        print("Id=",self.ID)
class Manager(Employee):
    def __init__(self,name,age,ID,salary):
        super().__init__(name,age,ID)
        self.salary=salary
    def display_man(self):
        self.display()
        print("Salary=",self.salary)
M=Manager("John",32,28043,5000)
M.display_man()
        
