a = float(input("Program will check 2 numbers and print the smallest. Enter first number:"))
b = float(input("Enter second number:"))

if a < b:
    print(f"Smallest number is: {a}")
elif a > b:
    print(f"Smallest number is: {b}")
else:
    print(f"Both numbers are eqcual: {a}")