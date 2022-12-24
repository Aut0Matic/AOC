import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append(line)


def solution1(array):
    return True

print("Part 1: ", solution1(list))
print("Part 2: ", solution2(list))