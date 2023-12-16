import sys
sys.setrecursionlimit(100000)

with open("data.txt", "rt") as myfile:
    lines = myfile.read().split('\n')

matrix = [[l for l in line] for line in lines]

def setup():
    global power, left, right, up, down
    power = [[l for l in line] for line in lines]
    left = [['.' for l in line] for line in lines]
    right = [['.' for l in line] for line in lines]
    up = [['.' for l in line] for line in lines]
    down = [['.' for l in line] for line in lines]

def iteration():
    result = 0
    for i, _ in enumerate(power):
        for k, _ in enumerate(power[i]):
            if power[i][k] == '#':
                result += 1
    return result                

moves = {('|', 'r'): [(-1, 0, 'u'), (1, 0, 'd')],
         ('|', 'l'): [(-1, 0, 'u'), (1, 0, 'd')],
         ('|', 'u'): [(-1, 0, 'u')],
         ('|', 'd'): [(1, 0, 'd')],
         
         ("\\", 'r'): [(1, 0, 'd')],
         ("\\", 'l'): [(-1, 0, 'u')],
         ("\\", 'u'): [(0, -1, 'l')],
         ("\\", 'd'): [(0, 1, 'r')],
         
         ('-', 'r'): [(0, 1, 'r')],
         ('-', 'l'): [(0, -1, 'l')],
         ('-', 'u'): [(0, -1, 'l'), (0, 1, 'r')],
         ('-', 'd'): [(0, -1, 'l'), (0, 1, 'r')],

         ('/', 'r'): [(-1, 0, 'u')],
         ('/', 'l'): [(1, 0, 'd')],
         ('/', 'u'): [(0, 1, 'r')],
         ('/', 'd'): [(0, -1, 'l')],

         ('.', 'r'): [(0, 1, 'r')],
         ('.', 'l'): [(0, -1, 'l')],
         ('.', 'u'): [(-1, 0, 'u')],
         ('.', 'd'): [(1, 0, 'd')]
         }
    
def beam(row, col, d):        
    # Check if we are trying to light up an invalid position
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1:
        return
    
    # Check if we have already been here:
    if d == 'l':
        if left[row][col] == '#':
            return
        else:
            left[row][col] = '#'
            
    elif d == 'r':
        if right[row][col] == '#':
            return
        else:
            right[row][col] = '#'

    elif d == 'u':
        if up[row][col] == '#':
            return
        else:
            up[row][col] = '#'
            
    elif d == 'd':
        if down[row][col] == '#':
            return
        else:
            down[row][col] = '#'
    
    # Light it up
    power[row][col] = '#'
    
    # Grab the character
    t = matrix[row][col]
    
    # Grab the moves.
    m = moves[(t, d)]
    
    # Perform all subsequent moves recursively
    for move in m:
        beam(row + move[0], col + move[1], move[2])

# Part 1
setup()
beam(0, 0, 'r')
r = iteration()   
print(r)

# Part 2
best = 0

for y in range(len(power)):
    setup()
    beam(y, 0, 'r')
    r = iteration()    
    best = r if r > best else best
    setup()
    beam(y, len(power[0])-1, 'l')
    r = iteration()
    best = r if r > best else best

    
    
for x in range(len(power[0])):
    setup()
    beam(0, x, 'd')
    r = iteration()        
    best = r if r > best else best
    setup()
    beam(len(power)-1, x, 'u')
    r = iteration()
    best = r if r > best else best
                
print(best)