#10. Iterators and Generators
#Iterators allow us to iterate through a sequence of element I.e, visiting each element once in a sequence
#We can pass any sequence to the iterator like list , string , tuple , set and dictionary
#visiting all the elements one by one in a list,tuple,set,dict is called as iteration

# there is a built in function called iter for iteration
print('Iterations in List')
L = [1,2,3,4,5] 

itr = iter(L)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr)) #shows error as the list contains only 5 elements

#iterations in tuple
print('\nIterations in tuple')
T = (1,2,3,4,5)

tup = iter(T)
print(next(tup))
print(next(tup))
print(next(tup))
print(next(tup))
print(next(tup))

#Iterations in set
S = {1,2,3,4,5}
print('\nIterations in set')
se = iter(S)

print(next(se))
print(next(se))
print(next(se))
print(next(se))
print(next(se))

#Iterations in dict
D = {'name':'Arun', 'age':25, 'profile':'Django'}
#shows only the keys in dict, values are ignored
print('\nIterations in dict')

di = iter(D)
print(next(di))
print(next(di))
print(next(di))

#Generators
#We can write our own iterators which are called “GENERATORS” they work just like iterators
print('\nGenerators in python')

def Days():
  D = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  i = 0
  while True:
    x = D[i]
    i = (i+1)%7
    yield x

d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))