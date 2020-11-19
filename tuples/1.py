from random import randint
t=(randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5))
print(t)
n=int(input("enter number between 1-5: "))
count=t.count(n)
print("your number exists: ",count)