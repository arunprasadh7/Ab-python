#Iterating a list - for loop, for loop with range, while loop
l1 = [5,6,7,8,9]
#for loop
for i in l1:
    print(i,end=" ")
print()

# for loop using range
for i in range(len(l1)):
    print(l1[i],end=" ")
print()

for i in range(len(l1)-1,-1,-1):
    print(l1[i],end=',')
print()

for i in range(-1,-(len(l1)+1),-1):
    print(l1[i],end='-')
print()

#while loop
i = 0
while i<len(l1):
    print(l1[i],end="/")
    i+=1
print()