# Try except and else block

print('Try block')

try:
  a = int(input('Enter a : '))
  b = int(input('Enter b : '))

  c = a//b 
  print('Try block executed successfully.')

except ZeroDivisionError as err:
  print(err)

else:
  print(f'Division is {c}')

print('Outside try-else block.')
