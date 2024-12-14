class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def validate_details(self):
        
        if not (self.student_id.startswith("STU") and len(self.student_id) == 7 and self.student_id[3:].isdigit()):
            return "It must start with 'STU' and be followed by 4 digits."

        
        if not (self.name.replace(" ", "").isalpha() and len(self.name) >= 2):
            return "Invalid Name."

        
        valid_grades = [f"{i}th Grade" for i in range(1, 13)]
        if self.grade not in valid_grades:
            return "Invalid Grade."

        return "All details are valid."

    def display_details(self):
        
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")


s_id = input("Enter the student ID: ").strip()
name = input("Enter the name of the student: ").strip()
grade = input("Enter the grade of the student (e.g., '1st Grade'): ").strip()

student = Student(s_id, name, grade)
validation_message = student.validate_details()

if validation_message == "All details are valid.":
    student.display_details()
else:
    print(validation_message)
