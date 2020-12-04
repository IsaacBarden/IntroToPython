#Taking input; concatenation
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + "'s favorite color is " + favorite_color)

#Type conversion
LBS_TO_KG = 0.4535924
weight_lbs = input("Weight in lbs: ")
weight_kg = LBS_TO_KG * float(weight_lbs)
print("Weight in kg: " + f"{weight_kg:.2f}")