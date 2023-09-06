#List meth
l1 = [5, 6, 7, 8, 9]
print(len(l1))

#append  - adding to the end - only one value can be added at a time
l1.append(10)
print(l1)
print(len(l1))
#l1.append(11, 12, 13) # erroe - append can only add one value at a time

#adding using slicing
l1[5:5] = [11]
l1[len(l1):] = [12]

#extend - to add multiple values at once
l1.extend([13,14,15]) #multiple values must be given within square brackets
print(l1)
print(len(l1))
l1.extend(['abc'])
print(l1)
l1.extend('abc') #iterable - splits each string element one by one
print(l1)

#using slicing
l1[len(l1):] = [16,17,18]
print(l1)

#insert(index number, value) - used to add values at specific index - takes 2 parameters
l2 = [5,6,7,8]
l2.insert(0,4)
print(l2)
l2.insert(len(l2),9)
print(l2)
#using slicing
l2[2:3] = [10]
print(l2)
l2[0:0] = [12]
print(l2)

#copy() - creates copy of the existing list and creates a new list
l3 = [1,2,3]
l4 = l3.copy()
print(l4)