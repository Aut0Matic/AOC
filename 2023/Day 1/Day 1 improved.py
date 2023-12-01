import re

def solveLine(line):
    # Turn the array into enumerable, 1:one, 2:two...
    for index, string in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], start=1):
        # Replace each string as: one -> one1one to maintain start and end characters
        line = line.replace(string, string + str(index) + string)
    # Find each digit and stick them into a string
    digits = re.findall('(\d)', line)
    # Return the first and last ones stuck together
    return int(digits[0] + digits[-1])


with open('Day 1.txt', 'r') as file:
    sum = 0
    for line in file:
        sum += solveLine(line.strip())
        
print(sum)