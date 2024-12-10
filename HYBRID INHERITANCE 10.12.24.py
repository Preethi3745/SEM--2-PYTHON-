
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Manager(Employee):
    def __init__(self, name, age, Id):
        super().__init__(name, age)
        self.Id = Id

    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("Emp Id:", self.Id)


class Developer(Employee):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept

    def displayDeveloperInfo(self):
        print("Department:", self.dept)


class TeamLeader(Manager, Developer):
    def __init__(self, name, age, Id, dept, teamsize):
        Employee.__init__(self, name, age)  
        self.Id = Id
        self.dept = dept
        self.teamsize = teamsize

    def displayTeamLeaderInfo(self):
        self.displayManagerInfo()
        self.displayDeveloperInfo()
        print("Team Size:", self.teamsize)



obj1 = TeamLeader("Niki", 30, 1877, "IT", 15)
obj1.displayTeamLeaderInfo()
