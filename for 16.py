A = float(input(" A "))
N = int(input(" N "))

while N <= 0:
	N = int(input(" N "))

intPart = 0
floatpart = 0
mul = 1

for x in range(1, N + 1):
	mul = mul * A
	intPart = int(mul)
	floatpart = mul
	if intPart == floatpart:
		print(mul)
	else:
		pass