import copy
'''
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
 '''
#Part 1.
import re
f = open('Day 5.txt', 'r');
lines = f.read().split('\n')
f.close()

# Setup stacks:
stack = [[],[],[],[],[],[],[],[],[]]
index = 0

# Function to print the stack!   
def printstack(s):
    for idx, x in enumerate(s):
        print(idx+1, x)

for i in reversed(range(0,8)):
    for k in range(0,9):
        if lines[i][4*k+1].isalpha():
            stack[k].append(lines[i][4*k+1])
printstack(stack)

stack2 = copy.deepcopy(stack)

printstack(stack2)    
instructions = lines[10:]
for i in instructions:
    #print(i)
    inst = i.split()
    # Move from A to B some times
    times = int(inst[1])
    A = int(inst[3])-1
    B = int(inst[5])-1
    
    for k in range(0,times):
        pop = stack[A].pop()
        stack[B].append(pop)
    
    #printstack(stack)
    
finalstring = ''
for i in range(0,9):
    finalstring+=(stack[i].pop())

print('Part 1: ', finalstring)

#Part 2.
print('Part 2')
temp = []
printstack(stack2)
for i in instructions:
    print(i)
    inst = i.split()
    times = int(inst[1])
    A = int(inst[3])-1
    B = int(inst[5])-1

    for i in range(0,times):
        pop = stack2[A].pop()
        temp.append(pop)
        
    for i in range(0, times):
        pop = temp.pop()
        stack2[B].append(pop)
        
    printstack(stack2)
        
finalstring2 = ''
for i in range(0,9):
    finalstring2+=(stack2[i].pop())

print('Part 1: ', finalstring)
print('Part 2: ', finalstring2)