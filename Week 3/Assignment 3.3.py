# 3.3 Write a program to prompt the user for a score using raw_input. 
# Print out a letter grade based on the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try:
	grade = raw_input("Enter Grade:")
	g = float(grade)
except:
    print "Enter a decimal number, please"
    quit()

if g >=0.9:
    print 'A'
elif g >=0.8:
    print 'B'
elif g >=0.7:
    print 'C'
elif g >=0.6:
    print 'D'
else:
    print 'F'
