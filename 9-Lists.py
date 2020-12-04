#Find largest number in list
numbers = [1, 5, 2, 7, 3, 6, 3, 5, 2, 7, 3, 7, 2, 18, 5, 2, 3, 7, 3]
greatest_number = 0

for number in numbers:
    if number > greatest_number:
        greatest_number = number

print(greatest_number)

print()

#2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Equivalent to [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

print()

#List methods
nums = [5, 7, 2, 4, 4]
print(nums)
nums.append(10)
print(nums)
nums.insert(0, 10)
print(nums)
print(nums.count(4))
nums.remove(4)
print(nums.count(4))
print(nums.index(7))
print(7 in nums)
nums.sort()
print(nums)

print()

#Remove duplicates
#numbers = [1, 5, 2, 7, 3, 6, 3, 5, 2, 7, 3, 7, 2, 18, 5, 2, 3, 7, 3]

for number in numbers:
    if numbers.count(number) > 1:
        for i in range(numbers.count(number) - 1):
            numbers.remove(number)

print(numbers)