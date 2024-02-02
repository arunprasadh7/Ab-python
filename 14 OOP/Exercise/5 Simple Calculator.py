# 5 Simple Calculator 
# add, sub, multiply,divide using staticmethod 


class Calculator:
    
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a - b
    
    @staticmethod
    def mul(a,b):
        return a * b
    
    @staticmethod
    def divide(a,b):
        return a/b
    

print(Calculator.add(5,5))
print(Calculator.sub(5,5))
print(Calculator.mul(5,5))
print(Calculator.divide(5,5))

a = 10
b = 20
print(Calculator.add(a,b))
print(Calculator.sub(a,b))
print(Calculator.mul(a,b))
print(Calculator.divide(a,b))