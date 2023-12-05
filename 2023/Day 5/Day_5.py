r = r2 = 0

#! PART 1

seeds, *sections = open('Day_5.txt').read().split("\n\n")

# Seeds: 49 21 ...
seeds = list(map(int, seeds.split(":")[1].split()))

# Each section is a "map" in the problem
for section in sections:
    ranges = []
    for line in section.splitlines()[1:]:
        # Each range is a 3 value list of (destination, source, count)
        ranges.append(list(map(int, line.split())))
    
    # We will use this to track the change in seeds 
    newseeds = []
    
    for seed in seeds:
        # For each seed
        for dest, source, count in ranges:
            # For each list of (destination, source, count)
            if seed in range(source, source+count):
                # If the seed lies within the range, perform the change
                newseeds.append(seed - source + dest)
                break
        else:
            # If it wasn't in the range, it maintains its position.
            newseeds.append(seed)

    # Update the seeds list for the next iteration
    seeds = newseeds

# The solution to part 1 is the minimum sorted seed
r = min(seeds)

#! PART 2

inputs, *sections = open('Day_5.txt').read().split("\n\n")

# Now the inputs are a range
inputs = list(map(int, inputs.split(":")[1].split()))

for i in range(0, len(inputs), 2):
    # (start, start+count)
    seeds.append((inputs[i], inputs[i]+inputs[i+1]))
    
seeds = []

# Again, each section is a "map" in the problem
for section in sections:
    ranges = []
    for line in section.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
        
    newseeds = []
    
    # Now we need to iterate while we still have existing seed ranges.
    while len(seeds) > 0:
        # Pop the last one off of the list.
        start, end = seeds.pop()
        
        for dest, source, count in ranges:
            # We are comparing two ranges:
                # source -> source+count
                # dtart -> end
            
            # The start of any overlap will be the maximum of either the start of a seed range, or the start of the source
            startOverlap = max(start, source)
            # The end of any overlap will be the minimum of either the end of a seed range, or the end of the source range (source+count)
            endOverlap = min(end, source+count)
            
            # Check if we have an overlap
            if startOverlap < endOverlap:
                # If we have an overlap, add to our new seeds:
                # (Start of overlap - Source position + Destination Position, End of overlap - source position + destination position)
                newseeds.append((startOverlap - source + dest, endOverlap - source + dest))
                if startOverlap > start:
                    # If the overlap started after the start of the seed range.
                    # We need to also add the back in the part of the seed range before the overlap
                    seeds.append((start, startOverlap))
                if end > endOverlap:
                    # And vice versa.
                    seeds.append((endOverlap, end))
                break
        else:
            # If there is nothing left to be done, add the remaining seed to the newseeds.
            newseeds.append((start, end))

    # Update the seeds with our newseeds positions.
    seeds = newseeds

r2 = min(sorted(seeds))[0]

print(r)
print(r2)