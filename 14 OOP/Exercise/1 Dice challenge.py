# 1 Dice  in games 

from random import *

class Dice:
    
    def __init__(self,sides):
        self.sides = sides
        
    
    def roll_dice(self):
        return randint(1,self.sides)
    

d1 = Dice(6)
print(d1.roll_dice())

d2 = Dice(12)
print(d2.roll_dice())