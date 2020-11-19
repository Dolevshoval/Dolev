from random import randint
t=[randint(1,10) for i in range(16)]
t=tuple(t)
print(t)
t1=(t[0:4])+(t[-4::])
print(t1)