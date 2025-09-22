#path = "..\Exercises\_08-FileHandling\dice_rolls.txt"
#path = "..\dice_rolls.txt"
import random


DiceRolls = [random.randint(1,6) for i in range(0, 10)]     # Creating a list of 10 simulated dice rolls using list

path = "..\python-programming-PHILIP-FORSTING\Exercises\_08-FileHandling\dice_rolls.txt"

# a)

print(DiceRolls)
with open(path, "w") as f:
    for i in range(len(DiceRolls)):
        f.write(str(DiceRolls[i]) + " ")
f.close()

# b)
DiceRolls.sort()
with open(path, "a") as f:
    f.write("\n")
    for i in range(len(DiceRolls)):
        f.write(str(DiceRolls[i]) + " ")
f.close()

# c) 
nrOf4 = DiceRolls.count(4)
with open(path, "a") as f:
    f.write("\n")
    f.write("Number of fours: " + str(nrOf4))