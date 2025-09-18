import numpy as np
def dist2P(P,Q) :
    p1, p2 = P
    q1, q2 = Q
    dist = np.sqrt(np.pow(p1+q1, 2) + np.pow(p2+q2, 2))
    return dist

#P = input(f"Enter point P, elements separated by space:").split()
#Q = input(f"Enter point Q, elements separated by space:").split()
#P = [float(i) for element in P]
#Q = [float(elements) for element in Q]

P = [0,0]
Q = [10, 3], [-1, -9], [10, -10], [4, -2], [9, -10]


for i in range(len(Q)):
    print(dist2P(P, Q[i]))

