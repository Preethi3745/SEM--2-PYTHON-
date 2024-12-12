'''#PROBLEM--1

class Password:
    def __init__(self, password):  
        self.password = password

    def display(self):
        if len(self.password) < 8:  
            return "Password must contain at least 8 characters"
        elif self.password.islower():  
            return "Password must contain an uppercase letter"
        elif self.password.isupper():  
            return "Password must contain a lowercase letter"
        elif self.password.isalpha():  
            return "Password must contain numbers"
        elif self.password.isalnum()or ' ' in self.password:
            return "Password must contain symbols"
        else:
            return "Password is valid"


user_password = input("Enter the password: ")
p = Password(user_password)  
print(p.display())'''


#STARTING WITH CAPITAL LETTER

class Password:
    def __init__(self, password):  
        self.password = password

    def display(self):
        if len(self.password) < 8:  
            return "Password must contain at least 8 characters"
        elif not self.password[0].isupper():
            return "Password must start with a capital letter"
        elif self.password.islower():  
            return "Password must contain an uppercase letter"
        elif self.password.isupper():  
            return "Password must contain a lowercase letter"
        elif self.password.isalpha():  
            return "Password must contain numbers"
        elif self.password.isalnum() or ' ' in self.password:
            return "Password must contain symbols"
        else:
            return "Password is valid"

user_password = input("Enter the password: ")
p = Password(user_password)  
print(p.display())


