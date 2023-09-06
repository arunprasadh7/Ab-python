#Find the most occuring items in a list
l1 = ['a','b','c','d','e','a','b','c','a','b','a']
result = []

for i in l1:
    times = (i,l1.count(i))
    if times not in result:
        result.append(times)
print(result) #to print all occurences
print(result[0]) #prints max number
print(result[:2]) #prints first two