while True:
    x = int(input("Enter a number, program will check sign:"))

    if x > 0.0: 
        print(f"number is positive")
    elif x < 0.0:
        print(f"number is negative")
    else:
        print(f"number is zero")