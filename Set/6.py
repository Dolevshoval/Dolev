d={1:10,2:20,3:30}
n=int(input("enter key: "))
if n in d:
    del d[n]
print (d)