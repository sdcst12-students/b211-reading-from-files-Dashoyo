#!python

'''
Note that string split can also be used to make use of data from
CSV (comma separated value) files.  These are often used as a standard
format for transferring data between spreadsheets!
'''

filename = "data02.csv"
file = open(filename,"r")
data = file.read()

'''
What do you think this is going to print?
'''
print(data)

'''
Let's split up the data into a list, one line at a time
'''
lineData = data.split("\n")
print(lineData)

'''
Now, we will split up each line into a list:
'''
newList = []
for line in lineData:
    print(f"The line before we split: {line}")
    tempList = line.split(',')
    print(f"The line as a list after we split: {tempList}")
    newList.append(tempList)

print("======")
print("The data as a list of lists!")
print(newList)
