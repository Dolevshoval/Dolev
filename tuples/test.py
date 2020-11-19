d={1:10,2:20,3:30,4:40}
print(d.keys())
print (d.values())
print(tuple(d.items()))
for i in tuple(d.items()):
    if i[1]==30:
        print (i[0])