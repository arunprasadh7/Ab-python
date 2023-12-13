# Negative Age Exception

# creating our own class for age error
class NegativeAgeError(Exception):
  def __str__(self):
    return 'Age must be greater than 0'

# function 

def stage(age):

  if age < 0:
    raise NegativeAgeError('Age should not be negative')
  
  elif age >= 0 and age < 13:
    print('Kid')
  
  elif age >= 13 and age < 20:
    print('Teen')
  
  elif age >=20 and age < 50:
    print('Young')
  
  else:
    print('Old')

age = int(input('Enter age : '))

try:
  stage(age)

except NegativeAgeError as e:
  print(e)