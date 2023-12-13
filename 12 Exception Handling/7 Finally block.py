# Finally block - executes all times

def div():
  try:
    a = int(input('Enter a value : '))
    b = int(input('Enter b value : '))

    c = a//b
    return c
  
  except ZeroDivisionError  as err:
    print(f'{err}: Denominator should not be 0.')
  
  finally:
    print('Finally block')

z = div()
print(f'Result : {z}')
