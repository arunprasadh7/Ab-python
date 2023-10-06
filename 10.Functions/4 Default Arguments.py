#Default Arguments
#default should be on the right side
#keyword should be on the right side
#defaults are created only once

def add(a, b=0, c=0):
    return a+b+c

print(add(5,5,5))   #3 args
print(add(5,5))     #2 args
print(add(5))       #1 arg

print(add(5,c=15))
# print(add(b=5, c=10, 2)) # positional args must be declared first
print(add(2,c=10, b=5))

#Default args are created only once

def additem(item, L=[]):
    L.append(item)
    return L

print(additem(1))
print(additem(2))
print(additem(3))
print(additem(4))

L1 = [5,6,7,8,9]
print(additem(10,L1))

print(additem(22))