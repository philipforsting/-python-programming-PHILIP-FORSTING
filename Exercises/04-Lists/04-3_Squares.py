import random
import matplotlib.pyplot as plt

# a)   Use list comprehension to create a list of squares from -10 to 10 (*)
y_squares = [i**2 for i in range(-10, 11)]

# b)   Plot this list using matplotlib. (*)
#x = list(range(len(y_squares)))
x = [i for i in range(-10, 11)] # creating list of x (-10, 10)
plt.plot(x,y_squares)
plt.title("The function x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()