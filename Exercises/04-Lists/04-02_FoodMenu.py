# a) list with the following elements: "vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"
food = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]

# b) list with the weekdays
weekdays = ["Mån", "Tis", "Ons", "Tor", "Fre"]

# c) create a food menu with each day corresponding to each food item and print it out.
menu = "Bambameny\n"
for weekdays, food in zip(weekdays, food):
    menu += f"{weekdays}: {food} \n"

print(menu)