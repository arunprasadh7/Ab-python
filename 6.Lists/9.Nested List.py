#Nested list in python
list1 = [10,20,['a','b',['c','d']],30,40]
print(list1[0])
print(list1[2])
print(list1[2][0])
print(list1[2][2])
print(list1[2][2][0])
print(list1[2][2][1])

#Matrix in list

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
C = []
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        S.append(A[i][j] + B[i][j])
    C.append(S)
print(C)