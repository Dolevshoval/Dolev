d={1:10,2:20,3:30,4:40,2:10,5:20}
d_new={}
for i in d:
    if d[i] not in d_new.values():
        d_new[i]=d[i]
print(d_new)