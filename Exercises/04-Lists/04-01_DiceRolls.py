import random

DiceRolls = [random.randint(1,6) for i in range(0, 10)]     # Creating a list of 10 simulated dice rolls using list comprehension
print(f"Unsorted rolls: {DiceRolls}")

# a) sort the list in ascending order
DiceRolls.sort()
print(f"Acending order: {DiceRolls}")

# b) sort the list in descending order
DiceRolls.sort(reverse = True)
print(f"Descending order: {DiceRolls}")

# c) find the maximum and minimum value in the list
# Dice roll list is already sorted in descending order so the maximum is at element 0 and the minimum is at -1 (wrapped)
print(f"Maximum: {DiceRolls[0]} \nMinimum {DiceRolls[-1]}") 