# Accessors(getters) & Mutators(setters)
# accessor - reading method
# mutator - writing method

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # accessor - getter
    def getLength(self):
        return self.length

    #mutator - setter
    def setLength(self,l):
        self.length = l

    def getBreadth(self):
        return self.breadth

    def setBreadth(self,b):
        self.breadth = b

    def perimeter(self):
        return 2 * (self.length * self.breadth)

    def area(self):
        return self.length * self.breadth


r1 = Rectangle(10,5)

print(r1.getLength())
print(r1.area())
r1.setLength(5)
print(r1.getLength())
print(r1.area())

print()

print(r1.perimeter())
r1.setBreadth(10)
print(r1.getBreadth())
print(r1.perimeter())