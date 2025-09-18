import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)


def draw_poly2(a=0, b=0, c=0): # y = a*x^2 + b*x + c
    y = [a*pow(x_,2) + b*pow(x_,1) + c for x_ in x]
    plt.plot(x,y)
    plt.title("y = ax + b lines")
    plt.xlabel("x")
    plt.ylabel("y")

draw_poly2(a=1, b=0, c=-3)
draw_poly2(a=0, b=4, c= -7)
plt.show()

# at 