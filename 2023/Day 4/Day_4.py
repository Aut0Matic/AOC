import re

# Results variables
r = r2 = 0

# Parsing the input into a matrix
matrix = [x for x in open('Day_4.txt').read().strip().split('\n')]

# Vector to track how many of each card we have
cardcounts = [1] * len(matrix)

for index, line in enumerate(matrix, start = 0):
    a, b = line.split('|')
    a = re.findall('\d+',a)
    a = a[1:] # winning numbers
    b = re.findall('\d+', b) # card numbers
    
    score = matches = 0
    
    # Search through the numbers in this card
    for num in b:
        
        # If the numbers is a match
        if num in a:
            
            # Keep track of it
            matches += 1
            
            # Correctly adjust the score
            if score < 1:
                score = 1
            else:
                score = score * 2
    r += score

    # Update the number of each card
    for i in range(1,matches+1):
        cardcounts[index+i] += cardcounts[index]

r2 = sum(cardcounts)

print("Part 1:", r)
print("Part 2:", r2)