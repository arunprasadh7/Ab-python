# Class Variables & Class Methods

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

    @classmethod
    def displayCount(cls):
        print(cls.count)


r1 = Rectangle(5,5)
print(r1.count)

r2 = Rectangle(1,10)
print(r2.count)

r3 =Rectangle(20,20)
Rectangle.displayCount()





