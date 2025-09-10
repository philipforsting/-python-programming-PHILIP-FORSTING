import math

x = int(input("Write a number. Program will detect if number is: \n 1.even or odd \n 2.divisible by 5 \n 3.divisible by 5 and odd: "))

odd = (x % 2)
devisible5 = x % 5

if odd == 1 and devisible5 == 0:
    print(f"{x} is divisible by 5 and odd")
elif devisible5 == 0:
    print(f"{x} is divisible by 5")
elif odd == 1:
    print(f"{x} is odd")
else:
    print(f"{x} is even")