import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append((line.rstrip().strip('-').strip(' ')))

print(list)

def solution1(array):
    return array

def solution2(array):
    return array

print("Part 1: ", solution1(list))
print("Part 2: ", solution2(list))