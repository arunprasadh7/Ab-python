# 2 Write a class circle and find perimeter and radius 

from math import pi

class Circle:
    
    def __init__(self,radius):
        self.radius = radius
        
    def perimeter(self):
        p = 2 * pi * self.radius
        return f'Perimeter of the circle is {p} cm.'
    
    def area(self):
        a = pi *self.radius * self.radius
        return f'Area of cirlce is : {a} sq.cm.'
    
c1 = Circle(5)
print(c1.perimeter())
print(c1.area())


c2 = Circle(7)
print(c2.perimeter())
print(c2.area())