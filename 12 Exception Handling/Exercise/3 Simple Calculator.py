# Simple Calculator 

# custom class 
class MissingOperator(Exception):
  pass

# cal function

def calculate(expression):
  
  operators = ['+', '-', '*', '/']
  l = expression.split()

  if l[1] in operators:
    print('Result :',eval(expression))
  
  else:
    raise MissingOperand('Missing operator between characters.')


expression = input('Enter the expression seperated by commas: ')

try:
  calculate(expression)

except MissingOperator as e:
  print(e)