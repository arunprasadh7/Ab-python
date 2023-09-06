#Tuple iterations & operators

#iterations can be done using loops
    #for loop
t1=('jack', 45, 38.6, False, 5+6j,'Jill', 45)

for i in t1:
    print(i)

for x in range(len(t1)):
    print(t1[x],end='/')

#while loop
i = 0
while i <len(t1):
    print(t1[i])
    i+=1

#operators on tuple are similar to lists
'''
index   -  []
slicing -  [:]
concatenation +
repeat *
membership - in 
membership - not in 
'''
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)
print(t1+tuple([7,8,9]))
print(t1 * 2)
print(3 in t1)
print(5 not in t1)
print(5 in t1)
print(1 not in t2)
