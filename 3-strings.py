#Difference between '' and "" string assignment
first_line = "She's an \"expert\"."
second_line = 'She\'s an "expert".'
print(first_line)
print(second_line)

print()

#Multi Line String
multi_line = '''
Hello,

We have reviewed your application and unfortunately will be pursuing other applicants at this time.

Best of luck,
SOFTWARE COMPANY
'''
print(multi_line)

#Other string characteristics
sample_str = "The 5th character (array ndex 4) is 5."
print(sample_str[4])
print(sample_str[-2])
print(sample_str[4:7])
print(sample_str[4:])
print(sample_str[:7])

print()

#Formatting strings
first = "John"
last = "Smith"
msg = f"{first} [{last}] is"
print(msg)

print()

#String methods (more at https://docs.python.org/3/library/string.html)
a_string = "a string"
print(len(a_string))
print(a_string.upper())
print(a_string.find('t'))
print(a_string.replace("string", "longer string"))
print("string" in a_string)
print("String" in a_string)