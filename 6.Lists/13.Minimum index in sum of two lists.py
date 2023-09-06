#Find the minimum index in sum of two lists
l1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
l2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']
index1 = len(l1)+1 #take any greater value than the length of list
index2 = len(l2)+1

for i in range(len(l1)):
    #print(i,end='-')
    index = l2.index(l1[i])
    #print(index)
    if i + index < index1 + index2:
        index1 = i
        index2 = index
print(l1[index1],index1+index2)