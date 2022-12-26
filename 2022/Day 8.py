# Open file
f = open('Day 8.txt', 'r')
grid = [row.strip() for row in f.readlines()]
f.close()

# Find dimensions
cols = len(grid[0])
rows = len(grid)

# Edges are all visible
visible = 2*cols + 2*rows -4

# Scores for part 2
scores = []

# Traverse the grid
for row in range(1, rows-1):
    for col in range(1, cols-1):
        # Height of the tree we are looking at
        tree = grid[row][col]
        
        # Generate arrays of tree heights in each direction
        left = [grid[row][col-i] for i in range(1,col+1)]
        right = [grid[row][col+i] for i in range(1, cols-col)]
        up = [grid[row-i][col] for i in range(1,row+1)]
        down = [grid[row+i][col] for i in range(1,rows-row)]
        
        # Part 1:
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            visible+=1
        
        # Part 2    
        score = 1
        for dir in (left, right, up, down):
            # use each directional array, find when we encounter a tree that is >= to our height
            dirscore = 0
            for i in range(0,len(dir)):
                if dir[i]<tree:
                    dirscore+=1
                else:
                    dirscore+=1
                    break
            score = score * dirscore
        scores.append(score)
            
print('Part 1', visible)
print('Part 2', max(scores))