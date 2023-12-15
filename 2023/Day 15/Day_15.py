with open("data.txt", "rt") as myfile:
    matrix = myfile.read().split(',')

# Take a string and perform the hashing operation
def hash(s):
    v = 0
    for c in s:
        # Ascii value
        v += ord(c)
        # Multiply by 17
        v*=17
        # Take the remainder when divided by 256
        v=v%256
        
    return v
        
r = 0

# Hash map
boxes = [{} for _ in range(256)]

# Iterate through all of the instructions
for s in matrix:
    # Part 1 is the sum of the hashes
    r+= hash(s)
    
    # If it is a remove operations
    if '-' in s:
        # Separating the label and the box number
        label = s.split('-')[0]
        box = hash(label)
        
        # See if the label is in the box, if so, remove it
        if label in boxes[box]:
            del boxes[box][label]
        
    # If it is an add/modify operations
    elif '=' in s:
        # Separating the label and the box number
        label, strength = s.split('=')
        box = hash(label)

        # Adding or modifying the strength
        boxes[box][label] = strength
    


r2 = 0

# Iterate through all boxes
for i, box in enumerate(boxes):
    # Iterate through all lenses in the box, fresh count at 0
    boxsum = 0
    for k, key in enumerate(boxes[i]):
        # Sum for this box (boxnum+1)*(boxposition)*(lense value)
        boxsum += (i+1)*(k+1)*int(boxes[i][key])
        
    # Add the sum to the total
    r2 += boxsum
    
print(r)
print(r2)