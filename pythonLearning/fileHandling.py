# working with text file
# python provide a file object to read text/binary files.


import os

print(os.path.abspath(os.curdir))

with open("myfile.txt", 'w') as f:
    f.write("this is my file \n")
    f.write("second line \n")
    f.write("I am Shipra \n")

# a for append

with open("myfile.txt", 'a') as f:
    f.write("this is my file \n")
    f.write("second line \n")

# r for read the file

with open("myfile.txt", 'r') as f:
    for line in f:
        print(line)
