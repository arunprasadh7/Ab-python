        #Set operators
s = {1,2,3,4,5,6,7,8,9,10}
a = {1,2,3,5,7}
b = {5,7,9,10,11}

print(a|b)      #Union  | pipe
print(a&b)      #intersection  &
print(a-b)      #difference -
print(a^b)      #symmetric difference ^

'''
<   -   to check proper subset
<=  -   to check subset
>   -   check proper superset
>=  -   check superset
==  -   check equal
!=  -   not equal
in  
not in 
'''

print('a is proper subset of s :',a<s)
print('a is subset of s :',a<=s)
print('s is subset of s :',s<=s)
print('s is equal to s :',s==s)
print('b is subset of s :',b<s)
print('s is subset of a :',s<a)
print('s is superset of a :',s>a)
print('a = b :',a==b)
print('a not equal to b :',a!=b)
print('10 in s :', 10 in s)
print('12 in s :',12 in s)
print('10 not in a :',10 not in a)
print('2 not  in a :',2 not in a)