# Brocode - moving a file

import os

source = 'move_file.txt'
destination = 'C:\\Users\\arun\\Desktop\\Abdul Bari Python\\13 File Handling\\BroCode files\\moved_file.txt'

try:
  if os.path.exists(destination):
    print(f'Filename {source} already exists.')
  
  else:
    os.replace(source, destination)
    print(f'{source} moved successfully.')

except FileNotFoundError:
  print(f'{source} not found.')