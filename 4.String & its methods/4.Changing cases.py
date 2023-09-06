#String methods - changing cases

#capitalize - changes the first letter of the string to capital/uppercase
s = 'hello world'
print( s.capitalize())
s1 = 'HELLO world'
print(s1.capitalize())

#lower() - changes to lower case
s2 = 'Hello World'
print(s2.lower())
s3 = 'HELLO HOW ARE YOU ?'
print(s3.lower())

#swapcase() - changes upper to lower and vice versa

a = 'HELLO world'
print(a.swapcase())

#title() - every letter of first word is converted to capital
b = 'hi , how are you ?'
print(b.title())

#casefold - similar to lowercase, used in special cases where characters
#do not have specific case (in german language)

c = 'HELLO'
c1 = 'hello'
print(c == c1)
print(c.lower()==c1.lower())

d = 'Bu\u00DF'
d1 = 'Buss'
print(d)
print(d.lower()==d1.lower())
print(d.casefold()==d1.casefold())