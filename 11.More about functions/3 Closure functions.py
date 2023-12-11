# Closure Functions
# - nested function
# - access non local variables
# - return nested function
# - caller class 

def closure(name):
  def greet():
    print('*' * 10)
    print(f'Hello {name}')
    print('*' * 10)
  return greet

c1 = closure('Arun')
c1()

c2 = closure('Prasadh')
c2()


# eg 2

def parent_function(name):
  coins = 3

  def play_game():
    nonlocal coins
    coins -= 1

    if coins > 1:
      print(f'{name} has {coins} coins left.')
    elif coins == 1:
      print(f'{name} has {coins} coin left.')
    else:
      print(f'{name} is out of coins.')
  
  return play_game

arun = parent_function('Arun')
arun()
arun()

arc = parent_function('Arc warden')
arc()
arc()
arc()