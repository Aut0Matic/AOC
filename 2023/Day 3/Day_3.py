import re
from collections import defaultdict

# Results variables
r = r2 = 0

# Parsing the input into a matrix
matrix = [x for x in open('Day_3.txt').read().strip().split('\n')]

# Dictionary of "gears" for part 2
gears = defaultdict(list)

# Non-symbol characters
digits = '0123456789.'

# Function to search for in a given space in the matrix (around a number)
def findsymbol(x1, x2, y1, y2, num):
    # Iterate up and down each col
    for y in range(y1, y2+1):
        # Iterate left and right across each row
        for x in range(x1, x2+1):
            # Check that the bounds are okay
            if y <= len(matrix)-1 and y >= 0 and x <= (len(matrix[y])-1) and x >= 0:
                # Gear number handling
                if matrix[y][x] == '*':
                    # We want to use a tuple as the key so we can check later if another number had the same gear location
                    gears[(y,x)].append(num)
                
                # Part 1, if we find a symbol we know to add it.
                if matrix[y][x] not in digits:
                    return True
    return False
    
# Use row as a variable to track which row we are on, line is the contents of the row
for row, line in enumerate(matrix, start=0):
    # Use a regex to match groups of digits on a line, there may be more than one.
    for match in re.finditer('\d+', line):
        # Grab the actual value of the number we found
        value = int(match.group(0))
        # Search in the bounds around it
        if findsymbol(match.start()-1, match.end(), row-1, row+1, value):
            # Increment part 1 solution
            r += value

# Look at each item in the dictionary
for i, j in gears.items():
    # If the list corresponding to a star location has 2 numbers, we multiply them and add the result to the part 2 result.
    if len(j) == 2:
        r2 += j[0] * j[1]

print("Part 1:", r)
print("Part 2:", r2)