        #Dictionary comprehensions
dict1 = dict()
print(type(dict1))
dict1['apple'] = 'red'
dict1['mango'] = 'yellow'

for x in range(1,6):
    dict1[x] = x**2
print(dict1)

d5 = {}
print(type(d5))
for x in range(1,6):
    d5[x] = x*2
print(d5)

d2 = dict(((1,2),(2,4),(3,6)))
print(d2)
d2 = dict(([1,11],[2,22],[3,33],[4,44]))
print(d2)
d2 = dict(('ab','cd','ef')) #only 2 args can be given
print(d2)
l1 = [(1,2),(3,4),(5,6)]
d2 = dict(l1)
print(d2)

a1 = ['a','b','c']
a2 = ['apple','ball','cat']
d3 = dict(zip(a1,a2))
print(d3)

b1 = {7,8,9}
b2 = 'AJK'
d3 = dict(zip(b1,b2))
print(d3)

d3 = dict(zip([10,20,30],[101,102,103,104,105]))
    #only takes pair values, ignores extra values
print(d3)

