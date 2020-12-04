#The ol' FizzBuzz
def FizzBuzz(number):
    return_val = ""
    if number % 3 == 0:
        return_val += "Fizz"
    if number % 5 == 0:
        return_val += "Buzz"
    if len(return_val) == 0:
        return_val += str(number)
    return return_val


end_num = 1
for i in range(end_num):
    print(FizzBuzz(i+1))

print()

#Using keywords, exceptions
def Store_Information(first_name, last_name, age, income):
    full_name = f"{first_name} {last_name}"
    try:
        risk = int(age) / int(income)
    except:
        print("Age or income invalid")
        return
    print(f"User {full_name} stored, calculated risk is {risk}")


first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
income = input("income: ")

Store_Information(age=age, income=income, first_name=first_name, last_name=last_name)