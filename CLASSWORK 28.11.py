class Employee:
    def getemployeeinfo(self):
        self.id=input("Enter the ID: ")
        self.name=input("Enter the Name: ")
    def displayemployeeinfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getdetails(self):
        self.getemployeeinfo()
        self.sal=int(input("Enter the salary: "))
    def displayinfo(self):
        print("salary= ",self.sal)
p=Perks()
p.getdetails()
p.displayinfo()
