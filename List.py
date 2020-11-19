from random import randrange
password=""
n=input("enter name: ")
list1=["a","b"]
for i in range (6):
    i=randrange(1,10) or randrange(list1)
    i=str(i)
    password+=i
print("Username: ",n,"\n","Password: ",password)