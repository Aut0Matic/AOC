# Part 1
f = open('Day 3.txt', 'r')
lines = f.read().split('\n')
f.close()

total = 0;

for i in lines:
    length = len(i)
    A = i[0:int(length/2)]
    B = i[int(length/2):length]

    priority = 0
    character = ''.join(set(A).intersection(B))
    if len(character)>0:
        priority = ord(character)-96
        if priority < 0:
            priority += 58
    total += priority
    
print(total)

# Part 2
print("PART 2")
total_2 = 0
i=0
while i<300:
    priority = 0;
    A = lines[i];
    B = lines[i+1];
    C = lines[i+2];
    character = ''.join(set(A).intersection(B).intersection(C))
    priority = ord(character)-96
    if priority<0:
        priority+=58
    i += 3
    total_2 += priority
print(total_2)