f = open('Day 4.txt', 'r')
lines = f.read().split()
f.close()

count = 0

for i in lines:
    first, second = i.split(',')
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]:
        count+=1
    elif second[0] <= first[0] and second[1] >= first[1]:
        count+=1

print("Part 1: ", count)

# Part 2.
count2=0
for i in lines:
    first, second = i.split(',')
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0]<=second[0] and first[1]>=second[0]:
        count2+=1
    elif second[0]<=first[0] and second[1]>=first[0]:
        count2+=1

print("Part 2: ", count2)

