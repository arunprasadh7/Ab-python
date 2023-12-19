# Static Methods

class Rectangle:

    count = 0

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    @staticmethod
    def isSquare(length,breadth):
        return  length == breadth


r1 = Rectangle(5,5)
print(r1.isSquare(5,5))

print(Rectangle.isSquare(10,10))