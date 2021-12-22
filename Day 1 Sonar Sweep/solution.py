import os
#text_file = open("input.txt", 'r')

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)