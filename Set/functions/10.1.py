def maxnum (n1,n2,n3):
    if n1>n2 and n1>n3:
        mm=n1
    if n2<n3 and n2>n1:
        mm=n2
    if n3>n1 and n3>n2:
        mm=n3
    return mm

q=int(input("enter number1: "))
w=int(input("enter number2: "))
e=int(input("enter number3: "))
print(maxnum(q,w,e))