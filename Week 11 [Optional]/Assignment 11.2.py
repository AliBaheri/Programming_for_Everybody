# Assignment 11.2 Write a program to look for lines of the form
# New Revision: 39772
# And extract the number from each of the lines using a regular
# expression and the findall()method.
# Compute the average of the numbers and print out the average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

count = 0
value = 0

for line in handle:
    if re.findall('^New Revision:\s[0-9]+', line):
        value = value + int(line.split()[2])
        count = count + 1
print "File: " + name
print "Average: " + str((value / float(count)))
