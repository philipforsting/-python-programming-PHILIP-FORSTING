weight = float(input("Program will recommend nr of pills based on weight and ange of child. Enter childs weight:"))
age = int(input("Enter child age:"))

if (weight > 40):
    print(f"Recommended nr of pills: 1 - 2")
elif (weight > 26):
    print(f"Recommended nr of pills: 1/2 - 1")
elif (weight > 15):
    print(f"Recommended nr of pills: 1/2")
else:
    print(f"pills not recommended for children under 15 kg")