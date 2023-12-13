# BroCode - copy a file

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

# making a copy of file in same destination
shutil.copyfile('copytestfile.txt', 'copy2.txt') #copyfile(source, destination)

# making a copy in other directory
shutil.copy('copy2.txt', '13 File Handling\BroCode files\copy_file.txt')


shutil.copy2('copytestfile.txt', '13 File Handling\BroCode files\copy_file2.txt')