# Open file
f = open('Day 9.txt', 'r')
instructions = f.read().split('\n')
f.close()

# Create a grid to mark where the tail has visited
ROWS = 2000
COLS = 2000

grid = [[0 for i in range(ROWS)] for j in range(COLS)]

headx = 1000
heady = 1000
tailx = 1000
taily = 1000
grid[tailx][taily] = 1

# Iterate through instructions
for instruction in instructions:
    # Seperate instruction into a direction and how many times we go that way
    dir = instruction[0]
    times = int(instruction[2:])
    
    # Loop times:
    for i in range(times):
        hx = headx
        hy = heady
        if dir == 'R':
            headx+=1
        elif dir =='L':
            headx-=1
        elif dir=='U':
            heady+=1
        elif dir=='D':
            heady-=1
        else:
            print('no direction!')

        # SAME TILE
        if headx == tailx and heady==taily:
            pass
        
        # Dragged directly up or down
        elif headx == tailx:
            if heady-taily==-2:
                taily-=1
            elif heady-taily==2:
                taily+=1
        
        # Dragged side to side
        elif heady == taily:
            if headx-tailx==-2:
                tailx-=1
            elif headx-tailx==2:
                tailx+=1
        
        # No change
        elif abs(headx-tailx) + abs(heady-taily) <= 2:
            pass

        # Diagonal movements
        else:
            tailx = hx
            taily = hy
        
        # Update grid
        grid[tailx][taily] = 1
        
# Solution
print('Part 1', sum([i.count(1) for i in grid]))