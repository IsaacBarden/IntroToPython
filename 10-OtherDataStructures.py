#Tuples (immutable lists) and unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates #This works with lists too
print(f"{x} {y} {z}")

print()

#Dictionaries (key value pairs)
student = {
    "name": "James",
    "age": 28,
    "completed_course": True
}
print(student["name"])
print(student.get("name"))
print(student.get("birthday"))
print(student.get("Grade", "Grade not found"))
student["age"] += 1
print(student.get("age"))
student["Grade"] = "B"
print(student.get("Grade", "Grade not found"))

print()

#Emoji converter
message = input(">")            #Get input
words = message.split(" ")      #Split into words
emojis = {
    ":)": "(❁´◡`❁)",
    ":(": "(┬┬﹏┬┬)"
}
output = ""
for word in words:
    output += emojis.get(word, word) + ""
print(output)