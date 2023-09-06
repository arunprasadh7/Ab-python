#String methods - splitting & joining

#s.replace(old,new[,count])
a = 'a-b-c-d-e'
print(a.replace('-','*'))
print(a.replace('-',','))
print(a.replace('-','.',2))

print('---------------')

#s.join(iterable)
s1 = 'abc'
s2 = 'xyz'
print(s1.join(s2))
print(s2.join(s1))
s3 = '/'
s4 = 'abc'
print(s3.join(s4))
print(s4.join(s3))

l1 = ['Ironman','batman','thor']
l2 = ','
print(l2.join(l1))

#split([sep[,max split]])
name1 = 'arun prasadh manokaran'
print(name1.split())
print(name1.split(' ',1))
name2 = 'arun-prasadh-manokaran'
print(name2.split('-'))
print(name2.split('-',1))
name3 = 'arun*prasadh*manokaran'
print(name3.split('*'))
print(name3.split('*',1))

#splitlines - based on new line characters
c = 'aaa\nbbb\tccc\rddd\feee'
print(c.splitlines())
print(c.splitlines(keepends=True))
print(c.split())
