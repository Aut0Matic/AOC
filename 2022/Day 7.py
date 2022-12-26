f = open('Day 7.txt', 'r')
lines = f.read().split('\n')
f.close()

path = '/home'
dirs = {"/home": 0}

for line in lines:
    # If there is a command.
    if line[0]=='$':
    
        # if listing, we don't care.
        if line[2:4]=='ls':
            pass
        
        # if changing directory.
        elif line[2:4]=='cd':
            
            # going home
            if line[5:6]=='/':
                path = '/home'
            
            # going back
            elif line[5:7]=='..':
                path = path[:path.rfind('/')]

            # going into new dir
            else:
                newDir = line[5:]
                path = path + '/' + newDir
                dirs.update({path:0})
    
    # if listing dir        
    elif line[0:3]=='dir':
        pass
    
    # if there is size data:
    else:
        # Grab file size
        size = int(line[:line.rfind(' ')])
        
        # identify what directory we are in.
        dir = path
        
        # traverse path back to home, adding the size of the newfound file to each directory.
        for i in range(path.count('/')):
            dirs[dir] += size
            dir = dir[:dir.rfind('/')]

# Part 1 setup
total = 0

# Part 2 setup
free = 70000000 - dirs['/home']
smallest = 70000000

for dir in dirs:
    
    # Part 1:
    if dirs[dir]<=100000:
        total+=dirs[dir]

    # Part 2:    
    if free + dirs[dir] >= 30000000 and dirs[dir] < smallest:
        smallest = dirs[dir]

print('Part 1:', total)
print('Part 2:', smallest)