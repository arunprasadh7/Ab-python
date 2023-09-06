#Operators on list part 1
# [], [:]

list1 = [1,2,3,4,5,6,7,8,9,10]

# [] - index
print(list1[5])
print(list1[-2])
list1[0] = 2    #over writing values
print(list1[0])
x = list1[0]    #reading string value to variable
print(x)

#slice - [start:stop:step] generates a new list, does not modify the existing list
print(list1[:])
print(list1[3:8])
print(list1[::-1])

list1[:3] = [20,30,40]
print(list1)
print('length =',len(list1))

list1[:3] = ['two','three']
print(list1)
print('length =',len(list1))

list1[:3] = ['one','two','three','four','five']
print(list1)
print('length =',len(list1))

list2 = [1,2,3,4,5,6,7,8,9,10]
list2[::3] = [11,22,33,44] # exact length must be specified while using step
print(list2)