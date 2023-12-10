# 2 Returning functions

# Passing Function as a parameter
def display():
  print('Hello World')

def fun(d):
  d()

fun(display)

# eg2
def add(x,y):
  print(x + y)

def sub(x,y):
  print(x-y)

def fun(f,x,y):
  f(x,y)

fun(add,5,5)
fun(sub,10,5)

# Function returning a function

def outer():
  def display():
    print('Hello Mr Handsome.')
  
  return display

d = outer()
d()