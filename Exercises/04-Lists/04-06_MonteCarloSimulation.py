import math
import random as rdm
import matplotlib.pyplot as plt


# a)
points_5000_x = [rdm.uniform(-1.0, 1.0) for i in range(0,10000000)]
points_5000_y = [rdm.uniform(-1.0, 1.0) for i in range(len(points_5000_x))]
points_5000_c = ["red" if (math.sqrt(points_5000_x[i]**2 + points_5000_y[i]**2) >= 1.0) else "blue" for i in range(len(points_5000_y))]

plt.scatter(points_5000_x, points_5000_y, c=points_5000_c)
plt.show()

# b)
print(points_5000_c.count("blue") / len(points_5000_x))
# the total plot resembles a rectagle and the blue dots resemble a circle. The fraction clould be calculated by dividing area of a circle with the area of a rectangle 
# with equal width
# fraction =
# = A_circle / A_rectagle =
# = (pi * (d/2)**2) / d**2 =
# = (pi * d**2 / 4) / d**2 =
# = pi / 4
