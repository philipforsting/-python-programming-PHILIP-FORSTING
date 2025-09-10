import math

sum = 0
i=0
n = int(input("Sum serieres, specify n: "))

while (i <= n):
#    sum += (1 / (2**i))
    sum += (-1)**i / (2*i + 1)
    i += 1

print(f"Sum of series: {sum}")