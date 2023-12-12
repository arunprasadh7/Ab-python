# Examples of execptions

# 1 Index error 
l = [10,20,30,40,50]
index = int(input('Enter index : '))

print(l[index])


# 2 ValueError & TypeError
# val = int('abc') value error
# res = 2 + '3'  type error

# 3 KeyError
d = {1:'a', 2:'b', 3:'c'}
key = int(input('ENter a key : '))
print(d[key])


# 4 ZeroDivisionError
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

ans = a/b
print(ans)