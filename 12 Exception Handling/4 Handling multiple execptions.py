# Handling Multiple Execptions

L = [10,20,30,40,50]

try:
  index = int(input('Enter index value : '))
  print(L[index])
  print('End of try block')

except IndexError as msg:
  print('Enter value between 1 - 4', msg)

except ValueError as msg:
  print('Enter only numeric values in the range of 1-4', msg)

except:
  print('Some Error occurred')

print('Terminated Successfully.')