import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append(int(line.rstrip()))
        
count = 0

for i in range(1,len(list)):
    if(list[i]>list[i-1]):
        count=count + 1

windowcount = 0
i = 3
while i < len(list):
    prevwindow = list[i-3] + list[i-2] + list[i-1]
    newwindow = list[i-2] + list[i-1] + list[i]
    
    if newwindow>prevwindow:
        windowcount = windowcount + 1
    i = i + 1

print("Part 1: ", count)
print("Part 2: ", windowcount)