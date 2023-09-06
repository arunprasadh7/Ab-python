#Operators on list
# +, *, in, not in
l1 = [1,2,3]
l2 = [7,8,9]

#print(l1 + l2)
l3 = l1 + l2
print(l3)

a = l1+[4] #adding new values to list
print(a)
l1.extend([4,5,6]) #adding multiple values to list
print(l1)
#print( l2+[11,12,13])
l2 = l2 + [11,12,13]
print(l2)

# *-operator
print( l1*3)

# in & notin
list1 = [1,2,3]
if 3 in list1:
    print("Found")
else:
    print("Not found")

if 5 not in list1:
    print("True")
else:
    print("False")