def solve(instructions, length):
    # Setup positions
    xs = [0] * length;
    ys = [0] * length;
    
    # Dictionary containing tuples of what location has been visited
    tail_visited = { (xs[-1], ys[-1]) }
    
    # iterate through moves:
    for(mx, my), distance in instructions:
        for _ in range(distance):
            
            # Move the head
            xs[0] += mx
            ys[0] += my
            
            for i in range(length - 1):
                dx = xs[i+1] - xs[i]
                dy = ys[i+1] - ys[i]
                
                # Diagonal movement
                if abs(dx) == 2 or abs(dy) == 2:
                    xs[i+1] = xs[i] + int(dx/2)
                    ys[i+1] = ys[i] + int(dy/2)
            
            tail_visited.add( (xs[-1], ys[-1]))
            
    return(len(tail_visited))
            
dirs = {'L': (-1,0), 'R': (1,0), 'U': (0,-1), 'D': (0,1)}

instructions = [(dirs[line[0]], int(line[1:])) for line in open('Day 9.txt')]

print('Part 1:', solve(instructions, 2))
print('Part 2:', solve(instructions, 10))