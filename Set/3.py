n=int(input("enter number: "))
d={}
for i in range (1,n+1,1):
    d.update({i:i*i})
print(d)