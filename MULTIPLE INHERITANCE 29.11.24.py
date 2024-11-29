class Employee:
    def __init__(self,name,emp_ID,position):
        self.name=name
        self.emp_ID=emp_ID
        self.position=position
    def show(self):
        print("Name: ",self.name)
        print("Emp_ID: ",self.emp_ID)
        print("Position: ",self.position)
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def display(self):
        print("Street: ",self.street)
        print("State: ",self.state)
        print("Country :",self.country)
class EmployeeDetails(Employee,Address):
    def __init__(self,name,emp_ID,position,state,street,country):
        super().__init__(name,emp_ID,position)
        Address.__init__(self,street,state,country)
    def display_both(self):
        self.show()
        self.display()
ed=EmployeeDetails("Jiya",100,"Manager","Gandhi Nagar","TamilNadu","India")
ed.display_both()
    
        
