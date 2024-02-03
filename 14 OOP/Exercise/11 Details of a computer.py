# 12 Details of a computer 
# Inner classes 

class Computer:
    def __init__(self,name,make,os):
        self.name = name
        self.cpu = self.CPU(make)
        self.os = self.OS(os)
    
    def __str__(self) -> str:
        return f'Name : {self.name} \nMake : {self.cpu.get_make()} \nOS : {self.os.get_os()}'
    
    class CPU:
        def __init__(self,make):
            self.make = make
        
        def get_make(self):
            return self.make
        
    class OS:
        def __init__(self,os):
            self.os = os
        
        def get_os(self):
            return self.os
        
c1 = Computer('MacBook','Apple','IOS')
print(c1)

c2 = Computer('Yoga','Lenovo','Windows 11')
print(c2)