# Nested try and except 
# no used often as the same can be achieved by using muliple except blocks

try:
  a = int(input('Enter a Value : '))

  try:
    b = int(input('Enter b value : '))

    try:
      c = a//b
      print(c)
    except ZeroDivisionError as err:
      print('Zero to Division :',err)

  except ValueError as e:
    print('Value error inner: ',e)


except ValueError as e:
  print('Value error outer:', e)