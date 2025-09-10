
# assignment a. Print out 6th multiplucation table
for i in range(0,11):       
    print(f"{i*6}", end = " ")



# let the user input the table, start and end of the table.
tableDesired = int(input("Which table are you interested in?"))
tableStart = int(input("Specify start of table:"))
tableEnd = int(input("Specify end of table:"))

print(f"Your {tableDesired}th multiplication table from {tableStart} to {tableEnd}:", end = " ")

for i in range(tableStart,tableEnd+1):       
    print(f"{i*tableDesired}", end = " ")


# print out a full multiplication table from 0 to 10.

for i in range(0,11):       
    for j in range(0,11):
        print(f"{i*j}", end = " ")
    print(f)