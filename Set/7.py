from random import randint
names=['Dolev','Linore','Oz']
grades=[94,35,64]
d={}
for i in range (3):
    n=names[randint(0,len(names)-1)]
    while n in d:
        n = names[randint(0, len(names) - 1)]
    g=grades[randint(0,2)]
    while g in d.values():
        g = grades[randint(0, len(grades) - 1)]
    d[n]=g
print (d)