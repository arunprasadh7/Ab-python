# 6 Customer Phone Number 
# using accessors/getters and mutators/setters

class Customer:
    
    def __init__(self,name,ph):
        self.uname = name
        self.ph = ph
    
        
    def getName(self):
        return self.uname
    
    def getPhone(self):
        return self.ph
    
    def setPhone(self,no):
        self.ph = no


c1  =  Customer('Arun',123)

print(c1.getName())
print(c1.getPhone())

c1.setPhone(456)
print(c1.getPhone())