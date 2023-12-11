from collections import Counter

with open("Day_11.txt", "rt") as myfile:
    data = [list(line.strip()) for line in myfile.readlines()]

# Take an input matrix and a number of spaces we will expand to
def solve(matrix, spaces):
    # Result
    r = 0

    # Coordinates and a set of updated coordinates for stretching.
    coords = []
    newcoords = []

    # Populate them
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == '#':
                coords.append([i,j])
                newcoords.append([i,j])

    # Loop from top to bottom.
    for i in range(0,len(matrix)):
        
        # Figure out if we have a blank row
        row = matrix[i]
        counter = Counter(row)
        if counter.get('#', 0) == 0:
            # All galaxies after this point will be have the distance increased
            for coordindex, c in enumerate(coords):
                if c[0] > i:
                    # Note that its spaces-1 because we "replace" 1->2 in part 1, 1->1000000 in part 2
                    newcoords[coordindex][0]+=spaces-1
        
    # Iterating left to right
    for i in range(0, len(matrix[0])):
        # We must first construct a column
        col = []
        for j in range(0, len(matrix)):
            col.append(matrix[j][i])
            
        # Then figure out if we have a blank column
        counter = Counter(col)
        if counter.get('#', 0) == 0:
            # All galaxies after this point will have the distance increased
            for coordindex, c in enumerate(coords):
                if c[1] > i:
                    # Again, this is spaces-1 because we are replacing the distance
                    newcoords[coordindex][1]+=spaces-1
                
    # Iterate through the coordinates such that we compare every pair once
    for i in range(0, len(newcoords)):
        for k in range(i+1, len(newcoords)):
            c1 = newcoords[i]
            c2 = newcoords[k]
            
            # figure out the horizontal and vertical distances between each
            r += abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])
    
    return r

# Part 1
print(solve(data, 2))

# Part 2
print(solve(data, 1000000))