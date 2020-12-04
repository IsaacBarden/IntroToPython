CONVERSION_FACTOR = 0.4535924
unit = input("[K]g or [L]bs? ").upper()
weight = input("Enter weight: ")

if unit == 'L':
    weight = float(weight) * CONVERSION_FACTOR
    print(f"Weight in Kg: {weight:.2f}")
elif unit == 'K':
    weight =  float(weight) / CONVERSION_FACTOR
    print(f"Weight in Lbs: {weight:.2f}")
else:
    print("Invalid units")