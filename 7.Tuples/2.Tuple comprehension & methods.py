#Tuple comprehension & methods #index() & count()

t1 = (x for x in range(10))
print(t1)
t1 = tuple(x for x in range(10))
print(t1)
#t2 = *(x for x in range(10))    #cant use starred expression
t2 = (*(x for x in range(10)),)
print(t2)
t3 = (*(x for x in range(1,10,2)),)
print(t3)
t4 = (*(x for x in 'python'),)
print(t4)
t5 = (*(x for x in 'PyThOn' if x.islower()),)
print(t5)
t6 = tuple(x for x in 'PyThOn' if x.islower())
print(t6)
t7 = tuple(x**2 for x in (1,2,3,4,5,7))
print(t7)

#methods
t8 = (1,2,3,4,5,4,5,6,7)
print(t8.count(4))
print(t8.index(4))  #gives the index of first instance of 4
print(t8.index(4,4))#gives the index of first instance of 4 starting from index4