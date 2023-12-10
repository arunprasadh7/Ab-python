#Nested functions


# 1 Functions as objects
def display(name):
  print('Hello',name)

# display()

d = display

d('Arun')
d('Prasadh')  

# 2 Nested Functions - function inside another function

def outer(name):
  def inner():
    print(f'Inner function \nIAS {name}')
  inner()

outer('Arun')
