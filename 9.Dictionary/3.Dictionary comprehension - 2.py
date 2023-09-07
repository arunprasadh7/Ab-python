        #Dictionary comprehensions

#enumerate - gives index to the elements and stores as a tuple
l1 = [10,20,30]
for i in enumerate(l1):
    print(i,end=' ')
print()

d1 = dict(enumerate(l1))
print(d1)

s1 = {10,20,30}
d2 = dict(enumerate(s1))
print(d2)

d3 = {x for x in range(1,11)}   #prints a set as there is only one value for x
print(d3)

d3 = {x:x**2 for x in range(1,6)}
print(d3)                   #prints dict (x:x**2) - 2 values

d3 = {(x,x**2) for x in range(1,6)}
print(d3)

L1 = {'a','b','c'}
L2 = {'apple','ball','catch'}
d4 = {x:y for x,y in zip(L1,L2)}
print(type(d4),d4)
d4 = {(x,y) for x,y in zip(L1,L2)}
print(type(d4),d4)
d5 = {x:y for x,y in enumerate(L2)}
print(type(d5),d5)
d6 = {x:y for x,y in enumerate(L1)}
print(type(d6),d6)

