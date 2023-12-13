# BroCode - delete a file in python

import os

path = 'removefile.txt'

# remove a file
# os.remove(path) #does not remove empty folders

# remove an empty folder
path = 'empty_folder'
# os.rmdir(path)  #does not remove folder containing files

#remove folder containing files

import shutil

path = 'empty folder'
shutil.rmtree(path) #deletes folder containing files