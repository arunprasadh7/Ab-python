#Checking and removing if there are any duplicates from the list
l1 = [1,2,3,4,5,1,2,3,4,5]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)