'''
[2/12/2012] Challange #4 [difficult]
today, your challenge is to create a program that will take a series of numbers (5, 3, 15), and find how those numbers can add, subtract, multiply, or divide in various ways to relate to eachother. This string of numbers should result in 5 * 3 = 15, or 15 /3 = 5, or 15/5 = 3. When you are done, test your numbers with the following strings:

4, 2, 8
6, 2, 12
6, 2, 3
9, 12, 108
4, 16, 64

For extra credit, have the program list all possible combinations. 

for even more extra credit, allow the program to deal with strings of greater than three numbers. For example, an input of (3, 5, 5, 3) would be 3 * 5 = 15, 15/5 = 3. When you are finished, test them with the following strings.

2, 4, 6, 3
1, 1, 2, 3
4, 4, 3, 4
8, 4, 3, 6
9, 3, 1, 7

'''
import itertools

# Generate all permutations of how a number series
# can be ordered.
orders = list(itertools.permutations([0, 1, 2], 3))

seriesList = []
operators = ['+', '-', '*', '/']

# Read in all series of numbers from the input file.
f = open('numbers.file', 'r')

print "\nHere are the numbers: "

# Save each number series as a list.
# Display each series.
for line in f:
  line = line.rstrip()
  print line
  series = line.split(', ')
  seriesList.append(series)
  # "4, 2, 8" is now ['4', '2', '8']

print "\nHere are all possible equations that can be built with those numbers:\n"

# For each series, build equations using all the possible ordering of operands
# and operators.  Then evaluate the string equation.  If true, print it.
for series in seriesList:
  for order in orders:
    for operator in operators:
      equation = "%s %s %s == %s" % (series[order[0]], operator, series[order[1]], series[order[2]])
      if (eval(equation)):
        print equation
  print ""
