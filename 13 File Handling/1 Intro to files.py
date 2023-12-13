# file handling 

# filehandler = open(filename, mode)
# modes
# r - read - throws error if the file does not exist
# w - write - deletes all data of existing file / creates new file if file does not exist
# a - append - writes to the end of existing file
# r+ - read and write
# w+ - write and read
# a+ - append and read
# x - to open file in exclusive creation mode


# read mode - r
file = open('13 File Handling/myfile.txt', 'r')

str1 = file.read(5)
print(str1)

str1 = file.read(10)
print(str1)

file.close()

# write mode - w 

file = open('13 File Handling/write_demo.txt', 'w')

file.write('Hello\n')
file.write('This is a demo file for writing mode.\n')
file.write('Write mode creates a new file if the file doesnt exist.')

file.close()

# append mode - a

file = open('13 File Handling/write_demo.txt', 'a')

file.write('\nThis is demo for append method')
file.write('\nAppend method adds content to the end of the existing file.')

file.close()