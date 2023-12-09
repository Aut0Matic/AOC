lines = [x for x in open('Day_9.txt').read().strip().split('\n')]

r = r2 = 0

for line in lines:
    # Grab the values in the line    
    vals = list(map(int, line.split(' ')))
    
    # 2d array where each row contains the differences in the values above it
    differences = [[]]
    # The first row is from our input
    differences[0] = vals
    
    index = 0
    
    # We need to iterate until we have a line that is all zeros
    while differences[index].count(0) != len(differences[index]):
        # Add a blank row
        differences.append([])
        # Iterate through the current row
        for i in range(1,len(differences[index])):
            # Find the differences and add them to the array
            differences[index+1].append(differences[index][i]-differences[index][i-1])

        # increment the index
        index+=1
        
    # Once we have computed the history for an input line, iterate through it backwards (bottom up)
    for i in reversed(range(1, len(differences))):
        # Extrapolate the future value
        differences[i-1].append(differences[i-1][-1]+differences[i][-1])
        # Extrapolate the previous value
        differences[i-1].insert(0, differences[i-1][0]-differences[i][0])
        
    # Part 1 is the sum of the top right value
    r+=differences[0][-1]
    # Part 2 is the sum of the top left value
    r2+=differences[0][0]
    
print(r)
print(r2)