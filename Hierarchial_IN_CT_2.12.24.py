class Teacher:
    def __init__(self,sub):
        self.sub=sub
    def show(self):
        print("Subject=",self.sub)
class Student(Teacher):
    def __init__(self,sub,name,num):
        Teacher.__init__(self,sub)
        self.name=name
        self.num=num
    def display(self):
        self.show()
        print("Name=",self.name)
        print("Roll Number=",self.num)
s=Student("Maths","Diana",37)
s.display()
class student2(Teacher):
    def __init__(self,sub,p_name,rol):
        Teacher.__init__(self,sub)
        self.p_name=p_name
        self.rol=rol
    def dis_parent(self):
        self.show()
        print("Parent Name=",self.p_name)
        print("Roll Number=",self.rol)
p=student2("English","John",21)
p.dis_parent()
        
