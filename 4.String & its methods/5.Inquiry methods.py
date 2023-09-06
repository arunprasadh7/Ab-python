# String inquiry methods - returns boolean value

a = 'HELLO'
print(a.isupper())

b = 'hello'
print(b.islower())

c = 'Hello How Are You?'
print(c.istitle())

d = 'hello123'
print(d.isalnum())

e = 'Hellopunumn'
print(e.isalpha())

f = '    '
print(f.isspace())

g = 'abd$12'
print(g.isascii())

#isidentifier - checks if the variable name is valid or not, returns true for keywords

h = '1length'
h1 = 'length1'
print(h.isidentifier())
print(h1.isidentifier())

#isprintable - checks if the characters in string are printable

i = 'Hello\n How are you ?' #\n -new line is not printable so returns false
i1= 'Hello, how are you ?'
print(i.isprintable())
print(i1.isprintable())

#isdecimal -returns true if the string contains numbers 0-9 without decimal point

g = '123'
print(g.isdecimal())
g1 = '123.45' #decimal point - returns false
print(g1.isdecimal())

#isdigit -returns true even if the string contains superscript & subscript

g.isnumeric() #retruns true if the string is any number
