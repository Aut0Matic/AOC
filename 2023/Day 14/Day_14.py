from collections import Counter
with open("data.txt", "rt") as myfile:
    matrix = myfile.read().split('\n')

# For debugging
def printmatrix():
    for l in matrix:
        print(*l)
    print()

def shift():
    
    # This operation simply shifts everything to the left in a matrix
    # We have already transformed the matrix such that this is the correct thing to do.
    for rowi, row in enumerate(matrix, start=0):
        
        i1 = 0
        i2 = 1
        
        while i2<len(row):

            if matrix[rowi][i1] == '.':
                
                if matrix[rowi][i2] == '.':
                    i2+=1
                    
                elif matrix[rowi][i2] == 'O':
                    matrix[rowi][i1] = 'O'
                    matrix[rowi][i2] = '.'
                    i1+=1
                    i2+=1
                    
                elif matrix[rowi][i2] == '#':
                    i1 = i2
                    i2 += 1

            elif matrix[rowi][i1] == 'O':
                
                if matrix[rowi][i2] == 'O':
                    i2 += 1
                    i1 += 1
                
                elif matrix[rowi][i2] == '#':
                    i1 = i2
                    i2 += 1
                    
                elif matrix[rowi][i2] == '.':
                    i2 += 1
                    i1 += 1
                
            elif matrix[rowi][i1] == '#':
                    i1 = i2
                    i2 += 1
    return

# Get the current result value for the matrix state.
def getresult():
    r = 0

    for i, l in enumerate(matrix, start=0):
        c = Counter(l)
        r+=c['O'] * (len(matrix)-i)
    
    print(r)


# Count the number of cycles
i = 0

# Store any cycles that we have seen previously
cycles = {}

# Boolean to track if we have found a cycle
found_cycle = False

# Complete 1000000000 steps 
while i < 1000000000:
    
    i += 1
    
    # Shift North
    # This is a transpose H -> V
    matrix = [list(row) for row in zip(*matrix)]
    # Now perform shifts 
    shift()
    matrix = [list(row) for row in zip(*matrix)] 
    
    #! Part 1 result
    if i==1:
        getresult()
    
            
    # Shift West    
    shift()

    # Shift South
    # Shift back to north south, but now we also need to reverse each row H -> V(r)
    matrix = [list(row) for row in zip(*matrix)]
    matrix = [list(row[::-1]) for row in matrix]
    shift()
    matrix = [list(row[::-1]) for row in matrix]
    matrix = [list(row) for row in zip(*matrix)]
    
    
    # Shift East
    
    # Back V(r) -> H(r)
    matrix = [list(row[::-1]) for row in matrix]
    shift()
    # H(r) -> V(r)
    matrix = [list(row[::-1]) for row in matrix]
    
    # Check if we have found a cycle.
    if not found_cycle and (found_cycle := str(matrix) in cycles):
        # length is equal to the number of iterations between the current iteration and where we last saw this pattern.
        cycle_length = i - cycles[str(matrix)]
        
        # increment the cycle count to the largest number that fits under this.
        i += cycle_length * ((1000000000 - i) // cycle_length)

    else:
        # This pattern hasn't been seen before, so lets store it.
        cycles[str(matrix)] = i

#! Part 2 result
getresult()