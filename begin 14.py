import math as m

L = int(input(" L: "))
while L == 0:
    L = int(input(" L: "))

R = L / (2*m.pi)
S = m.pi * pow(R,2)

print("R = ",R)
print("S = ",S)