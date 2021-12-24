import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append(int(line.rstrip()))

def solution1(array):
    for i in array:
        for k in array:
            if i+k==2020:
                return i*k

def solution2(array):
    for i in array:
        for k in array:
            for j in array:
                if i+k+j==2020:
                    return i*k*j
                
print("Part 1: ", solution1(list))
print("Part 2: ", solution2(list))