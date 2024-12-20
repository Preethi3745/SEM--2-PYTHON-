class Addition:
    def add(self, a, b, c=0,d=0):  
        sum1 =a+b+c+d
        return sum1

s = Addition()  
res = s.add(1, 2)  
print(res)
res1 = s.add(1, 2, 3)  
print(res1)
res2 = s.add(1, 2, 3, 5)  
print(res2)

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(300)

print("Total number of pages are:",b1+b2)
