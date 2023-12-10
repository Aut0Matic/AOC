# Parsing input
matrix = [x for x in open('Day_10.txt').read().strip().split('\n')]

# This keeps track of where pipes are
pipes = [[0] * 140 for _ in range(140)]

# Translating a direction and a pipe type into a new direction.
translate = {('N', '|'): 'N',
             ('S', '|'): 'S',
             ('E', '-'): 'E',
             ('W', '-'): 'W',
             ('S', 'L'): 'E',
             ('W', 'L'): 'N',
             ('E', 'J'): 'N',
             ('S', 'J'): 'W',
             ('E', '7'): 'S',
             ('N', '7'): 'W',
             ('N', 'F'): 'E',
             ('W', 'F'): 'S'}

# Find the position of S
for index, line in enumerate(matrix, start = 0):
    found = line.find('S')
    if found != -1:
        origin = (index, found)
        
# These are the positions of each pipe, we will iterate aroung the loop in both directions.
#! note: this assumes that the pipes are always vertical out of the origin, I am not sure if this is true.
p1 = (origin[0]-1, origin[1])
p2 = (origin[0]+1, origin[1])

# Set the locations to true for containing a pipe
pipes[origin[0]][origin[1]] = 1
pipes[p1[0]][p1[1]] = 1
pipes[p2[0]][p2[1]] = 1

# These are the starting directions into each pipe from S
d1 = 'N'
d2 = 'S'

# Number of pipes
count = 1

# Take a position, translate it into a unit vector in each direction
def newpos(d):
    if d == 'N':
        return (-1, 0)
    elif d == 'S':
        return (1, 0)
    elif d == 'E':
        return (0, 1)
    elif d == 'W':
        return (0, -1)

# While the pipes haven't met yet
while p1 != p2:
    # Find the new directions
    d1 = translate[(d1, matrix[p1[0]][p1[1]])]
    d2 = translate[(d2, matrix[p2[0]][p2[1]])]
    
    # Calculate new positions, this is just adding two tuples
    p1 = tuple(map(lambda i, j: i + j, p1, newpos(d1)))
    p2 = tuple(map(lambda i, j: i + j, p2, newpos(d2)))
    
    # Increment the number of pipes
    count+= 1

    # Map these onto our pipe matrix
    pipes[p1[0]][p1[1]] = 1
    pipes[p2[0]][p2[1]] = 1
    
# Number of enclosed cells for part 2
enclosed = 0

# Iterate through the matrix each row left to right
for i in range(0, 140):
    
    # At the start of each row, we consider that we are not enclosed
    er = False

    # Iterate right
    for j in range(0, 140):
        
        # If we find a pipe
        if pipes[i][j] == 1:
            
            # If the pipe is a vertical pipe or we are at the start
            if matrix[i][j] in "|JL" or matrix[i][j]=="S":
                # We toggle whether we are enclosed or not
                er = not er
        else:
            # If we are enclosed, we will add 1, else we add 0
            enclosed += er
            
print("part 1: ", count)
print("part 2: ", enclosed)