weight = float(input("Program will detect if luggage weight and dimensions are allowed. Enter weight:"))
dimList = []

dimList.append(float(input(f"Enter luggage length:")))
dimList.append(float(input(f"Enter luggage width:")))
dimList.append(float(input(f"Enter luggage height:")))

dimList.sort(reverse = True)
print(dimList)

if (weight <= 8.0) and (dimList[0] <= 55) and (dimList[1] <= 40) and (dimList[2] <= 23):
    print("Luggage allowed")
elif (weight > 8.0):
    print("Luggage to heavy")
elif (dimList[0] > 55) or (dimList[1] > 40) or (dimList[2] > 23):
    print("Luggage dimensions to big")