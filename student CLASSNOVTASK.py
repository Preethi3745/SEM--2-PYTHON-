#PROBLEM--1
class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age:  {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")

    def __del__(self):
        print(f"Student details for {self.name} are deleted.")
        
stu=Student("Susan",17,"AI","B")
stu.show()
del stu



#PROBLEM--2
class StudentInfo:
    def __init__(self, name, rollno, mark1, mark2, mark3):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_percentage(self):
        
        total = self.mark1 + self.mark2 + self.mark3
        percentage = (total / 300) * 100
        return percentage

    def show(self):
        
        percentage = self.calculate_percentage()
        print(f"\nName: {self.name}")
        print(f"Roll Number: {self.rollno}")
        print(f"Subject 1 Marks: {self.mark1}")
        print(f"Subject 2 Marks: {self.mark2}")
        print(f"Subject 3 Marks: {self.mark3}")
        print(f"Percentage: {percentage:.2f}%")

    def grade(self):
        
        percentage = self.calculate_percentage()
        print("\nGrade: ", end="")
        if percentage >= 90:
            print("A")
        elif percentage >= 80:
            print("B")
        elif percentage >= 70:
            print("C")
        elif percentage >= 50:
            print("D")
        elif percentage >= 40:
            print("E")
        else:
            print("F")



stu = StudentInfo("Susan", "33366", 99, 79, 67)
stu.show()  
stu.grade()
