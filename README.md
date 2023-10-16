## SDSS Computing Studies Python Assignment
### Assignment #8b Input/Output from Files (Total Marks 10)

Objectives:
* Read data from a file
* Store data to a file
* Use string.split() to separate the contents of a file into a list
* Develop an understanding of javascript object notation (json)
* Use the json library to retrieve or store complex data structures

We sometimes refer to volatile memory as memory stores where information is impermanent - when you turn off your computer, or when you close the program, the data stored in memory is gone.  There are several ways to deal with volatile memory that you want to keep:
1. We can save it to a file
2. We can store it in a database (which is really saving it to a file in a database)

Old methods would store the value of one variable per line in a text file, but these are very limited in their use.  It also doesn't really work well for more complex data structures like lists or tuples.  

##### Javascript Object Notation (JSON) #####
https://en.wikipedia.org/wiki/JSON
JSON is a way of storing complex data into text.  It is so useful that it has become quite standard to pass complex data between different applications using JSON.  A web page which uses Javascript to run its applications might send a request to a server that runs on Python or PHP.  That site will send data as JSON to the web page, where it is decoded and utilized in the Javascript environment.  JSON is very useful as a cross platform way of communicating! 

Today we will be reading and writing data from files.  There are many ways to read data from a file:
* You can read a whole file into a single variable. You can then split up the giant string using the .split() function
* You can read a file one line at a time, and store each line as an element of a list using the .readlines() function

### 5 Tasks

##### Task 1 Basic Search
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5

(2 points) 

##### Task 2 Pythaogorean Triples
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}

##### Task 3 Sum of Values
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787

##### Task 4 Advanced Dungeons and Dragons
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

##### Task 5 Stock Search
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches

(2 points)
