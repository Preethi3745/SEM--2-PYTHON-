class Calculator:
    def operator(self, a, b=None, c=None):
        if a != None and b ==None and c==None:
            return a * a
        elif a !=None and b !=None and c ==None:
            return a + b
        elif a!=None and b !=None and c !=None:
            return a * b * c
        
try:
    calc = Calculator()
    a = 5
    print("Answer:", calc.operator(a))
    a, b = 3, 4
    print("Answer:", calc.operator(a, b))
    a, b, c = 2, 3, 4
    print("Answer:", calc.operator(a, b, c))
except ValueError as a:
    print(f"Error: {a}")

