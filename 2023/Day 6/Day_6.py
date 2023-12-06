import math

lines = [x for x in open('Day_6.txt').read().strip().split('\n')]

def solve(times, distances):
    # We are performing iterative multiplication so the result starts at 1
    r=1
    
    # Iterate through the number of times
    for index in range(len(times)):
        t = times[index]
        distance = distances[index]
        
        # We are just solving a quadratic here:
        # (time - held)*held = distance
        # -held^2 +time*held - distance = 0
        #
        # The roots of this are
        # time/2 +- sqrt(time^2 - 4*distance)/(-2)
        
        # Floor function is used on the higher root
        high = math.floor(0.5* (t + (t**2 - 4* distance)**0.5))
        
        if (t-high)*high == distance:
            # If the high root ends up being equal to the distance, we don't count it
            high-=1
        
        # Ceiling function is used on the lower root
        low = math.ceil(0.5 * (t - (t**2 - 4* distance)**0.5))
        
        if (t-low)*low == distance:
            # If the low root ends up being equal to the distance, we count an extra
            low+=1

        # Count up the number of integer solutions
        r*=high-low+1
        
    # Return the cumulative product of solutions
    return r

# Part 1
times = [int(val) for val in lines[0].split() if val.isdigit()]
distances = [int(val) for val in lines[1].split() if val.isdigit()]

print(solve(times, distances))

# Part 2

# We still create 1 element arrays here because the solve function takes arrays.
times = [int(lines[0].split(':')[1].replace(' ', ''))]
distances = [int(lines[1].split(':')[1].replace(' ', ''))]

print(solve(times, distances))