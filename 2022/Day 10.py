# Grab instructions
instructions = [line.strip('\n') for line in open('Day 10.txt')]
# Setup variables
cycle = 0
register = 1
global strength
strength = 0

# crt monitor array
crt = [['.' for x in range(40)] for y in range(6)]

# Function to check if we are on a clock cycle that needs to update signal strength
def strengthUpdate(cycle, register):
    global strength
    if (cycle+20)%40==0:
        strength+=register*cycle

# Function to check if we need to draw a new pixel on the crt monitor
def drawCRT(cycle, register, crt):
    horizontal = cycle -1
    vert = 0

    # correcting for different lines
    while horizontal > 39:
        horizontal-=40
        vert+=1
    
    # Draw the pixel        
    if abs(horizontal-register)<2:
        crt[vert][horizontal]='#'

# Perform instructions
for instruction in instructions:
    # noop
    if instruction[0:4]=='noop':
        # no operation instruction takes 1 clock cycle
        cycle+=1
        
        # Perform checks after cycle
        drawCRT(cycle, register, crt)
        strengthUpdate(cycle, register)
    
    # addx
    elif instruction[0:4]=='addx':
        # Grab operand
        opperand = int(instruction[5:])
        cycle+=1
        
        # Perform checks after cycle
        drawCRT(cycle, register, crt)
        strengthUpdate(cycle, register)
        
        cycle+=1
        
        # Perform checks after cycle
        drawCRT(cycle, register, crt)
        strengthUpdate(cycle, register)
        
        # Update register at end of instruction
        register+=opperand

# Output solutions!
print('Part 1:', strength)
print('Part 2:')
[print(''.join(line)) for line in crt]