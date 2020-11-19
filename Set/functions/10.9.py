def zugi (list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i
    return (sum)

l=[]
for i in range (6):
    n=int(input("enter number: "))
    l+=[n]
print(zugi(l))