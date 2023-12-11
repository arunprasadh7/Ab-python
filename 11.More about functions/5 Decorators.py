# Decorators - passing function as parameter

def decorator(func):
  def wrapper(name):
    print('*' * 10)
    func(name)
    print('*' * 10)
  
  return wrapper

@decorator
def greet(name):
  print(f'Hello {name}')

# d = decorator(greet)
# d('Arun')

# display = decorator(greet)
# display('Storm')

greet('Invoker')
greet('Lion')
greet('Luna')