def limit (num,l_high,l_low):
    if num<l_high and num>l_low:
        return ("TRUE")
    else:
        return ("FALSE")

n=int(input("enter number: "))
l1=int(input("enter low limit: "))
l2=int(input("enter high limit" ))
if limit(n,l2,l1)=="TRUE":
    print("Success",n)
if limit(n,l2,l1)=="FALSE":
    print("Faild",n)