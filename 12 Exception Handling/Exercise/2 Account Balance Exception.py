# Account Balance Exception 

# creating custom error class
class AccountBalanceException(Exception):
  pass

# function to check balance 
balance = 1000

def withdraw(amount):
  c = balance - amount

  if c > 500:
    print(f'Withdrawl of {amount} Rs successful \nCurrent balance is {c} Rs.')
  
  else:
    raise AccountBalanceException('Minimum balance limit reached.')


amount = int(input('Enter withdrawl amount: '))

try:
  withdraw(amount)

except AccountBalanceException as e:
  print(e)