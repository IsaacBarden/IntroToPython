#Arithmetic operators, addition, multiplication, mod, power
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print()

#Incrementation
num = 10
print(num)
num += 3
print(num)
num *= 3
print(num)
num /= 3
print(num)

#Functions for working with numbers
import math

print()

#If statements and comparisons
first_name = input("Enter your first name: ")
if len(first_name) < 3 or len(first_name) > 50:
    print("very long or short name")
elif len(first_name) == 7:
    print("7 characters long")
else:
    print(f"Your name is {len(first_name)} characters long")    

