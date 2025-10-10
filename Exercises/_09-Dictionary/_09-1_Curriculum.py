curriculum = {
    "Examensarbete": 15,
    "LIA 1": 40,
    "LIA 2": 70,
    "Djup Maskininlärning": 40,
    "Data emngineering":45, 
    "Databaser": 25,
    "Maskininlärning":45,
    "Statistiskametorder":30,
    "Linjär algebra":20,
    "Databehandling":25,
    "Python":40,
    "Intro AI":5
}


sum = 0
for key, value in curriculum.items():
    sum += value

print(sum)