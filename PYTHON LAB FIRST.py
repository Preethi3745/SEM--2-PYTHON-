#Temperature Conversion

print("Enter 'c' to convert from Celsius to Fahrenheit")
print("Enter 'f' to convert from Fahrenheit to Celsius")
choice = input("Enter your choice:")
if choice =='c':
    celsius=float(input("Enter tempeerature in Celsius: "))
    fahrenheit=(celsius *9/5)+32
    print("%2f Celsius is:%0.2f Fahrenheit"%(celsius,fahrenheit))
elif choice=="f":
    fahrenheit=float (input("Enter temperature in Fahrenheit : "))
    celsius=(fahrenheit-32)*5/9
    print('%2f Fahrenheit is: %0.2fCelsius'%(fahrenheit ,celsius))
else:
    print("Invalid Input")


#Student Mark Processing

a=int(input("Enter the marks obtained in subject 1: "))
b=int(input("Enter the marks obtained in subject 2: "))
c=int(input("Enter the marks obtained in subject 3: "))
d=int(input("Enter the marks obtained in subject 4: "))
e=int(input("Enter the marks obtained in subject 5: "))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=50:
    print("Grade D")
elif per>=40:
    print("Grade E")
