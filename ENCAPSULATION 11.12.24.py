class Student:
    id=int(input("Enter the ID: "))
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print(f"Name: {self.__name}\n Age: {self.__age}")
s=Student("Eva",32)
s.display()
print(s.id)


class Employee:
    
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        
    def show(self):
       print("Name=",e.name)
       print("Salary=",e._Employee__salary)


class Manager(Employee):
    def __init__(self,name,salary,Id):
        Employee.__init__(self,name,salary)
        self.__Id=Id
        
    def display(self):
        self.show()
        print("Manager ID=",e._Manager__Id)
name=input("Enter the name: ")
salary=int(input("Enter the Salary: "))    
Id=input("Enter the ID: ")
e=Manager(name,salary,Id)
e.display()
