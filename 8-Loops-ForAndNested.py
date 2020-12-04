#Iterating through a string
for letter in "abacaba":
    print(letter == 'b')

print()

#Iterate through list
for name in ["John", "Paul", "George", "Ringo"]:
    print(name)

print()

#Iterate with given number
for number in range(5): #Note: This can accept things like range(5,10) -> [5,6,7,8,9] or range(5,10,2) -> [5,7,9]
    print(number)

print()

#Count up in base 3 (nested loop)
for MSB in range(3):
    for MB in range (3):
        for LSB in range(3):
            print(f"{MSB}{MB}{LSB}")

print()

#Make F shape
numbers = [5, 2, 5, 2, 2]

for number in numbers: #This runs faster than the actual solution
    print("x" * number)

#"Actual" solution
#for number in numbers:
#    for num_x in range(number):
#        print("x", end="")
#        if num_x == (number - 1):
#            print()
            