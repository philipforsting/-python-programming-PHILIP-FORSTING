import math

P1 = [2,1,4]
P2 = [3,1,0]

dist = math.sqrt((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2 + (P1[2]-P2[2])**2)

print(f"The distance is around {dist:.2f} l.u.")