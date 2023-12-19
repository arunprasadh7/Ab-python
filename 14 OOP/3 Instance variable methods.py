# Instance variables & Instance methods

# Instance variable changes from object to object/ instance
  # 3 ways to declare instance variables
    # - in constructor, inside method, outside class 
# Methods that access self are called instance methods

class Test:

  def __init__(self, a):
    self.a = a  #instance variable

  def sample(self):
    self.b = 10

t1 = Test(5)
print(t1.a)

t1.sample()
print(t1.b)

t1.c = 15
print(t1.c)