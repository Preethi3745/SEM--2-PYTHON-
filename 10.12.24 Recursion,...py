#Factorial using recursion:
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter the number: "))
print(f"The factorial of {factorial(num)}")


#COUNT 

def count_odd_even(number):
    odd_count = 0
    even_count = 0
    for num in number:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

n = input("Enter numbers separated by spaces: ")
number = []
for num in n.split():
    number.append(int(num))
    
result = count_odd_even(number)
odd_count, even_count = result

print(f"Odd numbers: {odd_count}")
print(f"Even numbers: {even_count}")
