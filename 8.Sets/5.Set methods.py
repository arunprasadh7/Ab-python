#Set methods - adding & deleting
s1 = {10,20,30,40,50}
print(s1)

#add() - to add one value to the set,
#       multiple values can be added using parenthis but will be stored as single
#       tuple inside the set
s1.add(60)      #adds 60 to set s1
print(s1)
s1.add((70,80)) #adds 70 & 80 to set s1 as single tuple
print(s1)

#copy() - creates copy of the mentioned set
s2 = s1.copy()
print(s2)

#update() - to add multiple values to set at once
s1.update({90,'james',100})
print(s1)
s1.update({'arun',10,20,30,100})  #duplicate values are excluded
print(s1)
s1.update('python')
print(s1)

                #removing elements from set
a = {1,2,3,4,5}

#pop() - will remove one random element from the set
a = {1,2,3,4,5}
print(a.pop())
print(a)

#discard() - remove the mentioned element from the set
#            if the element is not in set , ignores it
a = {1,2,3,4,5}
a.discard(4)    #removes 4
print(a)

#remove() - used to remove specific element from the set
#           if the element is not in set then throws error
a = {1,2,3,4,5}
a.remove(3)     #removes 3
print(a)

#clear() - clears all the contents of the set and returns empty set
a = {1,2,3,4,5}
a.clear()   #returns empty set
print(a)