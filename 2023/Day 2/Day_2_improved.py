# regex and math libs
import re, math

# Dictionary containing the maximum number of each colour or part 1
maxes = {'red': 12, 'green': 13, 'blue': 14}

# Solution variables for each part
part1 = part2 = 0

# enumeration of each id and the whole line
for id, line in enumerate(open('Day_2.txt'), start = 1):
    # Find each pair (number, colour) in each line
    pairs = re.findall(r'(\d+) (red|green|blue)', line)
    
    # If we don't have any number > the maxes dictionary for all of the pairs, add the id to the solution
    if not(any(int(pair[0]) > maxes[pair[1]] for pair in pairs)):
        part1 += id
    
    # Dictionary storing max values of red, green, and blue
    required = {'red': 0, 'green': 0, 'blue': 0}
    
    # Just splitting these
    for val, colour in pairs:
        # If the value for a colour is higher, set that as the new max in the dictionary
        required[colour] = int(val) if int(val) > required[colour] else required[colour]
            
    # Add the product of all values for colours of this line
    part2 += math.prod(required.values())
    
print("Part1: ", part1)
print("Part2: ", part2)