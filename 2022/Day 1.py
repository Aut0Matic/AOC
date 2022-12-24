# PART 1.
# Open the text file and read it all into an array line by line
f = open("Day 1.txt", 'r')
lines = f.read().split('\n')
f.close()

# Initialise the array that counts each elf's calories.
index = 0
counts = [0]

# Iterate through the file to sum each elf's calories
for i in range(0, len(lines)):

    # If the line contains a number
    if lines[i]!='':
        counts[index]+=int(lines[i]);
    # If blank line
    else:
        index+=1;
        # Need to append a new index so we have somewhere to write to!
        counts.append(0)

# Sort the list in reverse order.
counts.sort(reverse=True)

# Output solution to part 1.
print(counts[0])

# PART 2.
print(counts[0] + counts[1] + counts[2])