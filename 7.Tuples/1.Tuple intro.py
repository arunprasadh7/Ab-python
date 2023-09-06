#Tuples in python
#similar to list except they are read-only/immutable
#can contain duplicates
# are enclosed within ()

t1 = (1,2,3,4,5)
print(type(t1))
print(t1[2])
#t1[2] = 6      #cannot assign/modify the values of existing tuple
#print(t1[2])

t2 = () #creates an empty tuple
print(type(t2))

#packing of tuples
t3 = 1,2,3,4,5  #automatically packs values into a tuple
print(t3)
print(type(t3))
t4 = (10)       #single bracket - considers it as integer
print('t4',type(t4))
t5 = ((10))     #double brackets-considers it as tuple
print('t5',type(t5))
t6 = (10,)      #adding comma -considers it as a tuple
print(type(t6))

#Unpacking of tuple
a1 = (10,20,30,40,50)
a,b,c,d,e = a1
print(a)
print(b)
print(c)
print(e)

b1 = ([1,2,3])
print(type((b1)))
b2,c2,d2 = b1
print(b2)
print(type(b2))

c = (1,2,3,4,5)
#d1,d2,d3 = c #throws error because values on left does not match value count on right
# print(d1)
d1,d2,*d3 = c   #* assumes the values to the corresponding variable
print(d1)
print(d2)
print(d3)   #* assumes remaining values to d3
d1,*d2,d3 = c
print(d2)   #except first & last elements remaining are assigned to d2