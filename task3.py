#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

largest_sum = 0
current_sum = 0

with open('task03.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line: 
            current_sum += int(line)
        else:
            if current_sum > largest_sum:
                largest_sum = current_sum
            current_sum = 0

if current_sum > largest_sum:
    largest_sum = current_sum

print("The largest sum of points is:", largest_sum)
