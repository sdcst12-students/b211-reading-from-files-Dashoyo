#!python3

"""
We are going to open a file.  The open command allows you to
create a connection to a file.  There are two required parameters:
filename: a string literal that contains the name of the file to open
flag: a string literal that contains how the file will be handled.
Flag may be:
    'r' : read a file
    'a' : add to an existing file, but create it if it doesn't exist
    'w' : write to a file. Overwrites any existing data
    'x' : create a file for writing, but throw an error if it exists
"""
filename = 'data01.txt'
file = open(filename,'r')


'''
Note that if you determine the type of the file, it is not the standard
variable types that we have seen before.
'''
print(f"This file is of type: {type(file)}" )


'''
We can use the .read() method to get the contents of the entire file.
Below, we have stored it into a variable, but we could also print it directly
using a print command:
print( file.read() )
Note that the first part of the command is just the variable name that we are
using to handle the file stream data.
'''
data = file.read()
print("Full file data")
print("==============")
print(data)
print("")
'''
This data has line terminators that write the data on multiple lines.  The
line terminators are interpreted by Python as \n characters.
Note that we can use the string.split() command to break a string up into
a list.  It uses a 'delimiter' to determine where to make the breaks.
'''
myList = data.split('\n')
print(f"myList is now of type {type(myList)}")
print(myList)

'''
You can also read a file line by line and store each line as a list. 
Again, note that the lines will terminate with the \n character
'''
print("========================")
filename = 'data01.txt'
file = open(filename,'r')
data = file.readlines()
print(data)