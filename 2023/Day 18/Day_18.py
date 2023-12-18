with open("data.txt", "rt") as myfile:
    lines = myfile.read().split('\n')
    
# Determinant of a 2x2 matrix
def det(c1, c2):
    return c1[0]*c2[1] - c1[1]*c2[0]

# Shoelace Formula (https://en.wikipedia.org/wiki/Shoelace_formula)
def shoelace(points):
    area = 0
    
    for i, _ in enumerate(points):
        if i >= len(points)-1:
            break
        area += det(points[i], points[i+1])

    return area/2

# Direction coordinate mapping
directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
# Pt 2 conversions
conv = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

for part2 in [False, True]:
    arr = [(0, 0)]
    cursor = [0, 0]
    
    perimeter = 0
    
    for line in lines:
        # Just splitting the input lines apart
        a, b, c = line.split()
        
        if part2:
            # Remove excess characters
            c = c.strip("()#")
            # Grab the length
            l = int(f"0x{c[0:5]}",0)
            # Grab the direction
            adjustment = directions[conv[c[-1]]]
            
        else:
            l = int(b)
            adjustment = directions[a]
            
        for i in [0, 1]:
            cursor[i] += l*adjustment[i]
            
        arr.append(tuple(cursor))
        perimeter += l
            
    arr = list(reversed(arr))
    
    A = shoelace(arr)
    
    # Pick's Theorem (https://en.wikipedia.org/wiki/Pick's_theorem)
    interior = A - perimeter/2 + 1
    r = interior + perimeter
    print(int(r))
            