#Sets {} - heterogenous, unordered, no duplicates, growable, mutable
#
s1 = {1,2,3.4,'jack',3.4,'jack'}
print(s1)
print(type(s1))
#print(s1[0])    #throws error because sets are unordered
s2 = set((1,2,3,4,5))
print(s2)
s3 = set(('python'))
print(s3)
s4 = {10,20,30,40,50}
#s4[0] = 100     #throws error as there is no index number in set
s4.discard(50)  #removes 50 from the set
print(s4)
s4.add(60)      #adds 60 to the set
print(s4)
