#String methods -1

#find - used to find values in string
#syntax - s.find(sub[,start[,end]])

s = 'hello, how are you'

print(s.find('o'))
print(s.find('how'))
print(s.find('k'))  # if the character is not in the string then it returns -1
print(s.find('o',5))
print(s.find('o',9,17))

print("")
#rfind - find string values starting from right
#syntax - s.rfind(sub,[start, end])

print(s.rfind('o'))
print(s.rfind('o',0,15))
print(s.rfind('o',0,7))

print("")

# index - gives the index number of the character
#rindex - gives index number from right
print(s.index('o'))
print(s.index('o',6))
#print(s.index('k')) #if the given character is not in the string then throws error
print(s.rindex('o'))
print(s.rindex('o',0,12))

print("")

#count - counts the number of instances

print(s.count('o'))
print(s.count('l'))
print(s.count('are'))