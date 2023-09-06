#Concatenate all integer from string into a single number

l1 = [1,2,3,4,5]
s1 = ''
for i in l1:
    s1 += str(i)
print(int(s1))