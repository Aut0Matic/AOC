from functools import reduce
import math

lines = [x for x in open('Day_8.txt').read().strip().split('\n')]

r = r2 = 0
cycles = []
sequence = lines[0]
p2 = []
moves = {}

# Parsing the input
for i in range(2,len(lines)):
    # AAA = (BBB, CCC)
    key, inst = lines[i].split('=')
    key = key.replace(' ', '') # AAA
    inst = inst.replace(' ', '').replace('(', '').replace(')', '') # BBB,CCC
    
    left, right = inst.split(',') # left = BBB, right = CCC
    moves[key] = (left, right) # {'AAA': ('BBB', 'CCC')}
    
    # For Part 2 we need to start at all locations ending with A simultaneously
    if key.replace(' ','')[2] == 'A':
        p2.append(key)

# For Part 1 we start at AAA
current = 'AAA'

# Keep going until we reach ZZZ
while current != 'ZZZ':
    
    # We need to keep doing the sequence over and over again
    for i in sequence:
        
        # Left move
        if i == 'L':
            current = moves[current][0]
            
        # Right move
        else:
            current = moves[current][1]
            
        # Add another step
        r += 1
        
        # If we made it to the end
        if current == 'ZZZ':
            break

# For part 2 we are taking steps from all starting positions at the same time
for index, key in enumerate(p2, start = 0):
    current = key
    cycle = 0
    
    # Basically the same as above.
    while current[2] != 'Z':
        for i in sequence:
            if i == 'L':
                current = moves[current][0]
            else:
                current = moves[current][1]
            cycle += 1
                
            if current[2] == 'Z':
                break

    cycles.append(cycle)

# Find the lowest common multiple of all cycles, this will be the earliest they all line up.
r2 = reduce(math.lcm, cycles)

print(r)
print(r2)