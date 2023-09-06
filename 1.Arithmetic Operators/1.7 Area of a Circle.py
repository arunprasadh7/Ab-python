# Area of a circle

'''
# normal method
r = float(input("Enter the radius :"))
pi = 3.14
area = pi * (r**2)
print("Area of the circle is",area)
'''
#Using math module

import math

r = float(input("Enter the radius :"))
area = math.pi * r * r
print("Area of circle is",area)