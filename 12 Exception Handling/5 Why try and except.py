# Why try and except is used for exception handling

# case 1

def div(a,b):
  if b != 0:
    c = a/b
    return c
  else:
    return -1 #we assume value -1 to be zero division 
  
a = int(input('Enter a :'))
b = int(input('Enter b :'))

c = div(a,b)

if c == -1:
  print('Zero division Error')
else:
  print(c)

# the above method fails incase the division answer is -1
# eg -10/10 = -1 but in this case it shows as ZeroDivisionError

# case 2

def div(a,b):
  if b != 0:
    c = a/b
    return c
  else:
    raise ZeroDivisionError
  
a = int(input('Enter a :'))
b = int(input('Enter b :'))

c = div(a,b)

try:
  c = div(a,b)
  print(c)

except:
  print('ZeroDivisionError')