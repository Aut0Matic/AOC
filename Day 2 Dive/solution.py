import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append((line.rstrip()))

print(list)

horizontal = 0
vertical = 0

for i in list:
    if(i[0]=='f'):
        horizontal = horizontal + int(i[int(len(i))-1])
    if(i[0]=='d'):
        vertical = vertical + int(i[int(len(i))-1])
    if(i[0]=='u'):
        vertical = vertical - int(i[int(len(i))-1])
        
print("Part 1: ", horizontal*vertical)
