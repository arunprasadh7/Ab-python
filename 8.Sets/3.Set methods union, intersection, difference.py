#Set operations in mathematics - union, intersection, difference

a = {1,2,3,5,7}
b = {5,7,9,10,11}

print(a.union(b))
print(b.union(a))
print(a.intersection(b))
print(b.intersection(a))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#update -  updates the value to the corresponding set
print(a.intersection_update(b))
print(a.difference_update(b))
print(a.symmetric_difference_update(b))

#issubset, issuperset, isdisjoint
A = {1,2,3,4,5,6,7,8,9,10}
B = {1,2,3,5,7}
C = {4,6,8,10}

print(B.issubset(A))
print(C.issubset(A))
print(A.issuperset(B))
print(A.issuperset(C))
print(B.isdisjoint(C))