import numpy as np

path = "../python-programming-PHILIP-FORSTING/Exercises/_09-Dictionary/pokemon_list.txt"
pokemon_list = []
pokedex = {}
with open(path, "r", encoding="utf-8") as f_read:
    for line in f_read:
        row = line.split()
        pokedex[row[1]] = f"{row[2]}, {row[0]}"
f_read.close()
print(pokedex["Gengar"])
print(pokedex["Pikachu"])


