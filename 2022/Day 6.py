# Read file.
f = open('Day 6.txt', 'r')
line = f.read()
f.close()

# Iterate from the 3rd index to the end.
for i in range(4,len(line)):
    # Isolate 4 characters, turn them into a set(remove duplicates)
    base = line[i-4:i]
    new = set(base)
    # If there are 4 unique characters finish. 
    if len(new)==4:
        print("Part 1: ", i)
        break
        
for i in range(14,len(line)):
    # Isolate 4 characters, turn them into a set(remove duplicates)
    base = line[i-14:i]
    new = set(base)
    # If there are 4 unique characters finish. 
    if len(new)==14:
        print("Part 2: ", i)
        break
        