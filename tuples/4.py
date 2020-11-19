from random import randint
list= [randint(1,100) for i in range(10)]
t=tuple(list)
print(t)
print(type(t))
