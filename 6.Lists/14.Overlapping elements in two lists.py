#Overlapping elements in two lists
l1 = [10, 15, 6, 9, 12, 8, 4]
l2 = [14, 6, 19, 4, 7, 10, 11]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)