import numpy as np

def ChangePrintout(value=0):
    denominations = [1000, 200, 50, 20, 10, 5, 2, 1]
    for i in denominations:
        if value/denominations[i] >= 1: print(f"{value//denominations[i]}st {denominations[i]}-lapp") 
        value = value % denominations[i]

ChangePrintout(int(input("Enter a value and the change will be displayed: ")))