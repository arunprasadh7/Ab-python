# Operators on string- Concatenation, indexing, indexing, slicing, in, not in

#Indexing
s1 = 'Hello World'

for i in range(len(s1)-1,-1,-1):
    print(s1[i],end="")
print("")

for i in range(0,len(s1),2):
    print(s1[i],end="")
print("")

# Slicing [start:stop:step]
s2 = 'Hello World'
print(s2[0:])
print(s2[:len(s2):1])
print(s2[::2])
print(s2[3:])