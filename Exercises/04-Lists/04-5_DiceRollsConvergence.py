import random as rdm
import matplotlib.pyplot as plt

rdm.seed(1) 
# a) 100 dice rolls and count the number of outcome six
DiceRolls_100= [rdm.randint(1,6) for i in range(0, 100)]
print(f"The number of outcome six in 100 dice rolls is: {DiceRolls_100.count(6)}")


# b) 10, 100, 1000, 10000, 100000, 1000000 dice rolls. 
# Count the number of outcome six in each simulation and store it in a list. Compute the probability of outcome six in each simulation.
num_rolls = [10, 100, 1000, 10000, 100000, 1000000] # just for plot.
sixes = []
sixesP = []
for j in range(1,7): 
    sixes.append([rdm.randint(1,6) for i in range(0, 10**j)].count(6))

for j in range(len(sixes)):
    sixesP.append((float(sixes[j]) / (10**(j+1))))


print(f"Count number of six: {sixes}")
print(f"P(six) = {sixesP}")

# c) 
plt.plot(sixesP, '-*')
plt.title("Probability of six for different number of rolls")
plt.xticks([0,1,2,3,4,5], num_rolls)
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")
plt.show()