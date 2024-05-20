A = int(input(" A: "))
B = int(input(" B: "))
C = int(input(" C: "))

minimal = 0

if A < B and A < C:
	minimal = A

if B < A and B < C:
	minimal = B

if C < A and C < B:
	minimal = C

print('minimal - ',minimal)