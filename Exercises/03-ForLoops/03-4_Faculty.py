# Use a for statement to compute n! Let the user input n!
# n! = 1*2*3*...*(n-1)*n

n = int(input("Specify n in faculty calculation"))
fak = 1
for i in range (1,n+1):
    fak *= i

print(f"{fak}")