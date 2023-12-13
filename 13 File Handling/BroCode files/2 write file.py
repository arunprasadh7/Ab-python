# BroCode - write a file

with open('13 File Handling\BroCode files\write_demo.txt', 'w') as file:
  file.write('Hell0\nThis is a newly written file.')


# Appending to a file - a

with open('13 File Handling\BroCode files\write_demo.txt', 'a') as file:
  file.write('\nThis is also newly appended text.')

with open('13 File Handling\BroCode files\write_demo.txt', 'a') as file:
  file.write('\nThis is second appended line.')