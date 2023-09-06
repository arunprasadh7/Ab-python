#Adding two matrix

l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
l3 = []

for i in range(len(l1)): #range(3)-3 elements are there in l1
    s = []
    for j in range(len(l1[0])): #range(4) - 4 elements are inside l1[0]
        s.append(l1[i][j] + l2[i][j])
    l3.append(s)
print(l3)
