#Indexing & sorting
l1 = [5,6,7,5,8,9,6,10,6,5]

#index(x[,start[,end]]) - gives the index of the first occurence of the element
print(l1.index(8))
print(l1.index(6)) #gives the index of first occurence of 6
print(l1.index(6,2)) #gives the first occurence of 6 starting from index 2
print(l1.index(5,1,4))
#print(l1.index(6,2,5)) # throws error of the element is not in the list

l2 = [5,6,7,5,8,9,6,10,6,5]

#count method - counts the number of occurences of an element in a list
print(l2.count(5))

#reverse - prints the list in reverse order
print(l2.reverse())

#sort method - used the sort the list
print(l2.sort()) #by default sorts in ascending order
print(l2.sort(reverse=True)) #sorts in descending order
#alternatively sorted method is also used