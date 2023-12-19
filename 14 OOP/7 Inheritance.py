# Inheritance - process of acquiring features of an existing class into a new class

# Constructors in inheritance - super().__init__()

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth


class Cuboid(Rectangle):

    def __init__(self,length, breadth, height):
        super().__init__(length,breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height


c1 = Cuboid(10,10,10)
print(c1.perimeter())
print(c1.area())
print(c1.volume())