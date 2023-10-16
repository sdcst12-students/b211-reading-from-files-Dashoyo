#!python3

'''
We can also write data to a file using the file.write() command.
We first need to open the file using open(filename,flag)
where flag can be "w" or "a"
'''

filename = 'newFile.txt'
file = open(filename,'w')
print(f"We have opened a file with variable type:{type(file)}")

inputData = None
while inputData != "":
    inputData = input("Enter something to write")
    file.write(inputData + "\n")
'''
We should close the file when we are finished with it.
Note that data may not be written unless you close the file!

Let's now take a look at the data in our newFile.txt. You may notice
that it doesn't look as expected.  We might want to add some line breaks
for each line!

We might change line 16 of our program to read:
file.write(inputData + "\n")

This will add a linebreak to our text!
'''
file.close()
