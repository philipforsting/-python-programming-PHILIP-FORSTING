# a)
path = "../python-programming-PHILIP-FORSTING/Exercises/_08-FileHandling/test_result_org.txt"
with open(path, "r") as f_read:
    testResultData = f_read.read()
f_read.close()


# b)
resultData_list = testResultData.split("\n")
resultData_list.sort()          # sort
print(resultData_list)



path = "../python-programming-PHILIP-FORSTING/Exercises/_08-FileHandling/test_result.txt"
with open(path, "w") as f_write:
    for name in range(len(resultData_list)):
        f_write.write(str(resultData_list[name] + "\n"))
f_write.close()

# c)


resultData_list_sortedgrades = sorted(resultData_list, key=lambda x: int(x.split()[-1]))
"x.split() delar strängen på mellanslag → ['Adam', 'Gustafsson', '25']"
"x.split()[-1] tar sista elementet i listan → '25'."

with open(path, "a") as f_append:
    for name in range(len(resultData_list_sortedgrades)):
        f_append.write(str(resultData_list_sortedgrades[name] + "\n"))
f_write.close()