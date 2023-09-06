#List comprehension - ways of creating a list

#simple way of creating a list
l0 = []
for x in range(10):
    l0.append(x)
print(l0)

#L1 = [expression for item in iterable]
l1 = [x for x in range(10)]
print(l1)
l2 = [x**2 for x in range(1,6)]
print(l2)
l3 = [x for x in (10,5,7,8,12,3) if x%2==0]
print(l3)
l4 = [x.lower() for x in 'Python']
print(l4)
l5 = [x for x in '@Ar,un P%r*a$s@adh' if x.isalpha()] #prints only alphanumeric chatacters
print(l5)

#creating a string by getting input from the user
data = input('Enter names : ')
l6 = data.split()
print(l6)

l7 = input('Enter names :').split()
print(l7)