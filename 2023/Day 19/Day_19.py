from copy import deepcopy

with open("data.txt", "rt") as myfile:
    sections = myfile.read().split('\n\n')
    
rules = sections[0].split('\n')
parts = sections[1].split('\n')

# Dictionary has the name of a ruleset as key and an array of subsequent instructions as value
dictionary = {"A": "A", "R": "R"}

# Populate the dictionary
for rule in rules:
    name, rest = rule.strip('}').split('{')
    rest = rest.split(',')
    
    dictionary[name] = rest

#! Part 1
r = 0
    
for part in parts:
    # Iterate through all of the parts and grab each of the values
    p = part.strip("}{").split(',')
    x = int(p[0][2::])
    m = int(p[1][2::])
    a = int(p[2][2::])
    s = int(p[3][2::])
    
    # bool to check if we still need to iterate
    op = True
    
    # Now pass it into the instruction set
    instruction = "in"
    while op:
        insts = dictionary[instruction]
        for i in insts:
            if i == 'A':
                r += x + m + a + s
                op = False
                continue
            elif i == 'R':
                op = False
                continue
            elif i.find(':') == -1:
                instruction = i
                continue
            else:
                expression, outcome = i.split(':')
                if eval(expression):
                    instruction = outcome
                    break
                else:
                    continue
        
translate = {"x>": 0, "x<": 1, "m>": 2, "m<": 3, "a>": 4, "a<": 5, "s>": 6, "s<": 7,}

global r2
r2 = 0

# Recursively search bounds and calculate a hypercube volume
def recurse(rule, vec):
    # Result stored here
    global r2
    
    # We need to consider every instruction in a ruleset
    for i in dictionary[rule]:
    
        # If it is R we reject
        if i == 'R':
            # Reject
            continue
        
        # If it is A we add a hypercube volume to the total
        elif i == 'A':
            # Calculate the volume of the hypercube
            combinations = 1
            for i in range(0, 8, 2):
                combinations *= vec[i+1]-vec[i] + 1
            r2 += combinations

        # In this case we just have a literal instruction to go to (usually at the end)
        elif i.find(':') == -1:
            recurse(i, vec)
        
        # Here we need to cut it apart and execute on a new restriction:  
        else:
            
            # Copy the existing vector
            v = deepcopy(vec)
            
            # get the expression and outcome:
            expression, outcome = i.split(':')
            
            # Calculate the index
            index = translate[expression[0:2]]
            
            # If the index is 0, 2, ... it is a lower bound
            if (index + 2)% 2 == 0:
                # Set the lower bound to the value + 1
                v[index] = int(expression[2::]) + 1
                
                # Set the original upper bound to this value (this considers the case that this doesn't pass)
                vec[index+1] = int(expression[2::]) 
            else:
                # Set the uppe rbound to the value - 1
                v[index] = int(expression[2::]) - 1 
                
                # Set the original lower bound to this value (this considers the case that this doesn't pass)
                vec[index-1] = int(expression[2::])
            
            # Figure out if this is a violation or not.
            for k in range(0,8,2):
                if v[k]>v[k+1]:
                    # Handling the case by sending it to a fail
                    recurse('R', v)
                    continue
            
            # This one is evaluating in the case it is true
            recurse(outcome, v)
            
            
            # Note:
            # On the next iteration of the main loop, we will have the adjusted values in vec[] that represent the current case not passing
            # (Hence we had to move to the next instruction)

# First case for Part 2
recurse("in", [1, 4000, 1, 4000, 1, 4000, 1, 4000])

# Results
print(r)
print(r2)