
import os

list = []

with open('input.txt') as file:
    for line in file:
        list.append((line.rstrip()))

gamma = "0b"
epsillon = "0b"
ox = "0b"
co2 = "0b"

# Part 1

for i in range(0,12):
    counter = 0
    for k in list:
        if k[i]=="0":
            counter = counter + 1
    if counter>500:
        gamma = gamma + "0"
        epsillon = epsillon + "1"        
    elif counter<500:
        gamma = gamma + "1"
        epsillon = epsillon + "0"
        
consumption = int(gamma,2)*int(epsillon,2)

# Part 2

co2list = []
oxlist = []

for i in list:
    co2list.append(i)
    oxlist.append(i)

for i in range(0,12):
    oxtarget = '0'
    oxcount = 0
    for k in oxlist:
        if k[i]=='1':
            oxcount = oxcount + 1
    if oxcount>.5*len(oxlist):
        oxtarget = '1'
        
    co2target = '0'
    co2count = 0
    for k in co2list:
        if k[i]=='1':
            co2count = co2count + 1
    if co2count<0.5*len(co2list):
        co2target = '1'
    
    print("oxcount: ", oxcount, "oxtarget: ", oxtarget, "co2count: ", co2count, "co2target: ", co2target)

    if len(oxlist)>1:
        oxlist[:] = [x for x in oxlist if(x[i]==oxtarget and len(oxlist)>1)]
    if len(co2list)>1:
        co2list[:] = [y for y in co2list if(y[i]==co2target and len(co2list)>1)]
    
    
ox = ox + oxlist[0]
co2 = co2 + co2list[0]

print(ox, co2)

life_support = int(ox,2)*int(co2, 2)

print("Part 1: ", consumption)
print("Part 2: ", life_support)

print(oxlist)
print(co2list)