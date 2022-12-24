# Part 1.
# Read the file's lines in to an array.
f = open('Day 2.txt', 'r');
lines = f.read().split('\n')
f.close()

# Lookup table with dictionary
'''
A X -> R R -> D = (3 + 1) = 4
A Y -> R P -> W = (6 + 2) = 8
A Z -> R S -> L = (0 + 3) = 3
B X -> P R -> L = (0 + 1) = 1
B Y -> P P -> D = (3 + 2) = 5
B Z -> P S -> W = (6 + 3) = 9
C X -> S R -> W = (6 + 1) = 7
C Y -> S P -> L = (0 + 2) = 2
C Z -> S S -> D = (3 + 3) = 6
'''

outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

# Iterate through lines.
total = 0
for i in lines:
    total += outcomes[i]

# Part 1 solution
print(total)

# PART 2.
'''
A X -> L -> R S = 3
A Y -> D -> R R = 4
A Z -> W -> R P = 8
B X -> L -> P R = 1
B Y -> D -> P P = 5
B Z -> W -> P S = 9
C X -> L -> S P = 2
C Y -> D -> S S = 6
C Z -> W -> S R = 7
'''
newOutcomes = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}
total = 0
for i in lines:
    total += newOutcomes[i]
    
print(total)