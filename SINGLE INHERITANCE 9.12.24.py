
#PROBLEM--1
class Camera: 
    def __init__(self, quality, resolution): 
        self.quality = quality 
        self.resolution = resolution 
 
    def cam_info(self): 
        print(f"Quality: {self.quality}\nResolution: {self.resolution}") 
class Phone: 
    def __init__(self, phone_no): 
        self.phone_no = phone_no 
 
    def display(self): 
        print(f"Phone Number: {self.phone_no}") 
class Smartphone(Camera, Phone): 
    def __init__(self, quality, resolution, phone_no, model, brand): 
        Camera.__init__(self, quality, resolution)   
        Phone.__init__(self, phone_no)   
        self.model = model 
        self.brand = brand 
 
    def show(self): 
        self.cam_info() 
        self.display() 
        print(f"Model: {self.model}\nBrand: {self.brand}") 
s = Smartphone("48 MP", "4K", "220838271", "iPhone Pro Max", "Apple") 
s.show() 
 
#PROBLEM--2 
class Student:  
    def __init__(self,name,course):  
        self.name=name  
        self.course=course 
          
    def stu_Info(self):  
        print("Student Name:",self.name)  
        print("Course:",self.course)  
          
class StudentAthelete(Student):  
    def __init__(self,name,course,sports):  
        Student.__init__(self,name,course)  
        self.sports=sports  
     
    def display(self):  
        self.stu_Info()  
        print("Sports :",self.sports)  
s=StudentAthelete("Preethi","Artificial Intelligence","Tennis")  
s.display()
