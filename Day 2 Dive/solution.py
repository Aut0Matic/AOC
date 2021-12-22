import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append((line.rstrip()))

horizontal = 0
depth = 0

for i in list:
    val = int(i[int(len(i))-1])
    if(i[0]=='f'):
        horizontal = horizontal + val
    if(i[0]=='d'):
        depth = depth + val
    if(i[0]=='u'):
        depth = depth - val
        
print("Part 1: ", horizontal*depth)

horizontal = 0
depth = 0
aim = 0

for i in list:
    val = int(i[int(len(i))-1])
    if(i[0]=='f'):
        horizontal = horizontal + val
        depth = depth + aim*val
    if(i[0]=='d'):
        aim = aim + val
    if(i[0]=='u'):
        aim = aim - val

print("Part 2: ", horizontal*depth)