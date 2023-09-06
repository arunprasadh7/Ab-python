#Quadriatic expresssion
import math
a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c = int(input("Enter value of c :"))
#formula
r1 = complex((-b + math.sqrt(b**2)-(4*a*c))/2*a)
r2 = complex((-b - math.sqrt(b**2)-(4*a*c))/2*a)

print("Roots of the above equation are :",r1,r2)