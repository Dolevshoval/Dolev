d={}
grades={'dolev':80,'oz':70,'linore':60,'soshi':95,'dilo':84}
avg=sum(grades.values())/len(grades)
print("the average is: ",avg)
for i in grades:
    if grades[i]>avg:
        d[i]=grades[i]
print("pass: ",d)


