#String methods - removing elements
#pop([i]), remove(x), clear()

l1 = [5,6,7,8,9]
#pop() - by default removes the last element of the list
l1.pop()
print(l1)
l1.pop(0) # removes the first element
print(l1)
l1.pop(2)
print(l1)

#by using del keyword /similar to slicing
l2 = [1,2,3,4,5,6,7,8]
del l2[:5]
print(l2)
del l2[1:]
print(l2)

#remove(x) - the value to be removed must be given inside bracket, not index
l3 = [1,2,3,1,2,3,1,2,3]

l3.remove(1) #if multiple entries for an element are there, then it removes first instance
print(l3)
l3.remove(2)
print(l3)
#l3.remove(5) #if the elements to be removed is not in the list, then throws error
#print(l3)

#clear() - clears entire list and returns empty list
l4 = [1,2,3,4,5,6]
l4.clear()
print(l4)
del l4[:]
print(l4)

