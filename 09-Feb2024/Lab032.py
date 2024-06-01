import math

print(math.pi)
print(math.isqrt(4))
print(math.cbrt(8))

r = float(input("enter radius"))
# area = math.pi*(r**2)
area = math.pi * (pow(r, 2))
print(area)
print(math.cbrt(r))

print(max(2, 3, 4))
print("max number is: ", max(r, 3, 4))
