import random
with open('otazky.txt') as f:
    lines = f.readlines();
    while(len(lines)>0):
        while(input()!=""):
            x=0
        out = lines.pop(random.randint(0,len(lines)-1))
        print(out.split(".",1)[1])
    