import re

def reLine(line):
    line = re.sub('one', 'o1e', string=line)
    line = re.sub('two', 't2o', string=line)
    line = re.sub('three', 't3e', string = line)
    line = re.sub('four', 'f4r', string = line)
    line = re.sub('five', 'f5e', string = line)
    line = re.sub('six', 's6x', string = line)
    line = re.sub('seven', 's7n', string = line)
    line = re.sub('eight', 'e8t', string = line)
    line = re.sub('nine', 'n9e', string = line)
    return line

file_path = 'Day 1.txt'

with open(file_path, 'r') as file:
    
    sum = 0
    
    for line in file:
        stripped = line.strip()
        # print(stripped)
        stripped = reLine(stripped)
        # print(stripped)
        length = int(len(stripped))
        for i in range(0,length):
            if stripped[i].isdigit():
                low = stripped[i]
                # print("low: ",low)
                break
        
        for i in range(length-1, -1, -1):
            if stripped[i].isdigit():
                high = stripped[i]
                # print("high: ",high)
                break
            
        pair = int(str(low) + str(high))
        # print(pair)
        
        sum += pair
        
print(sum)