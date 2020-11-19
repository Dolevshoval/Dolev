def summ (n):
    #     n=list
    m=0
    for i in n:
        m+=n[i-1]
    return (m)

list=[]
for i in range (5):
    f=int(input("enter number: "))
    list+=[f]
print(summ(list))
