# 9 Inheriting shapes in challenges 
# Inheritance 

import math 

class Polygon:
    def __init__(self,ns,*sides):
        self.ns = ns
        self.sides = sides[:ns]
        

class Triangle(Polygon):
    def __init__(self, ns, *sides):
        Polygon.__init__(self,ns,*sides)
    
    def area(self):
        a,b,c = self.sides
        s = (a + b + c)/2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        return round(area,2) #corrected to 2 decimal places
        
    

t1 = Triangle(3,10,15,9)
print(t1.area())

t2 = Triangle(3,10,15,9,7,7,7,7,7,7)
print(t2.area())