file_path = 'Day_2.txt'

maxes = {'red': 12, 'green': 13, 'blue': 14}

sum = 0
power = 0

# PART 1
with open(file_path, 'r') as file:
    for line in file:
        b = False
        id = int(line.split()[1].strip(':'))
        sum += id
        print("Game ", id, " Sum = ", sum)
        arr = (line.strip().split(';'))
        for i in arr:
            j = i.split(',')
            # print(i)
            for problem in j:
                fin = (problem.strip())
                if(fin[0]=="G"):
                    fin = fin.split(':')[1].strip()
                
                val, key = fin.split()
                if(int(val) > maxes[key]):
                    sum -= int(line.split()[1].strip(':'))
                    print("Game ", id, " invalid (", val, " > ", maxes[key], "), sum = ", sum)
                    b = True
                    break
                
                if(b):
                    break
            if(b):
                break
            
        b = False
            
# PART 2
with open(file_path, 'r') as file:
    for line in file:
        arr = (line.strip().split(';'))
        r = 0
        g = 0
        b = 0
        for i in arr:
            j = i.split(',')
            # print(i)
            for problem in j:
                fin = (problem.strip())
                if(fin[0]=="G"):
                    fin = fin.split(':')[1].strip()
                
                val, key = fin.split()
                if(key[0]=='r' and int(val)> r):
                    r = int(val)
                if(key[0]=='g' and int(val)> g):
                    g = int(val)
                if(key[0]=='b' and int(val)> b):
                    b = int(val) 
                    
        power += r*b*g

   

print("Part 1: ", sum)
print("Part 2: ", power)