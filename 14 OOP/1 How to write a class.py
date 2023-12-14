# How to write a class 

# lets write a class for cuboid

class Cuboid:
  
  def __init__(self, l, b, h):
    self.length = l
    self.breadth = b
    self.height = h

  def lid_area(self):
    return self.length * self.breadth

  def total(self):
    return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)

  def volume(self):
    return self.length * self.breadth * self.height


c1 =  Cuboid(5,5,5)
print(c1.volume())