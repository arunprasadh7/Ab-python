# BroCode - read a file

with open('13 File Handling\write_demo.txt') as file:
  print(file.read())

print(file.closed) #returns True if the file has been closed

# the above method doesnt errors in case of exception

try:
  with open('write_demo.txt') as file:
    print(file.read())

except FileNotFoundError as e:
  print(e,'\nCheck file directory and try again.')