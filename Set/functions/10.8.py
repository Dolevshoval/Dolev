def rishoni (num):
    for i in range (2,10):
        if num%i==0:
            return "False"
        else:
            return "True"
n=int(input("Enter Number"))
print(rishoni(n))