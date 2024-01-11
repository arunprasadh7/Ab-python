# Method overloading - used to achieve polymorphism 
# writing more than one method with same name & perform different operations

class Arith:
    def sum(self,x,y):
        return x + y
    

# adding 2 ints
a1 = Arith()
print(a1.sum(10,5))

# adding 2 float 
a2 = Arith()
print(a2.sum(5.5,4.5))

# adding strings 
a3 = Arith()
print(a3.sum('Arun','Prasadh'))

print('--------------------------------')

# having 2 methods with the same name 
# the last method with the name will be considered and the previous ones will be ignored 
class Addition:
    def sum(self,a,b):
        return a + b

    def sum(self,a,b,c): 
        return a+b+c


add1 = Addition()
print(add1.sum(5,5,5))

# add2 = Addition()
# print(add2.sum(5,5)) #throws error

# overloading a method 
class  OverAdd():
    def sum(self,a,b,c=None):
        s = a + b
        if c == None:
            return s
        else:
            return s + c
    

oa1 = OverAdd()
print(oa1.sum(2,2))

oa2 = OverAdd()
print(oa2.sum(2,2,2))