
def nameCleaner(rawInput:str):
    rawInput = rawInput.strip()
    rawInput = rawInput.title()
    return rawInput


uncleanInput = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]
for i in range(len(uncleanInput)):
   print(nameCleaner(uncleanInput[i]))
