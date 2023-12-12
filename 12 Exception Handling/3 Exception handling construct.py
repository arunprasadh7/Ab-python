# Exception handling construct

# 1 IndexError

l = [10,20,30,40,50]

try:
  index = int(input('Enter the index value : '))
  print(l[index])
  print('End of try block')

except :
  print('Index value is out of range. Enter number between 1 - 4.')

print('Terminated gracefully')
