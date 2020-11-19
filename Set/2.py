d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d={}
d.update(d1),d.update(d2),d.update(d3)
n=int(input("enter key: "))
if n in d.keys():
    print("Exist")
    print(d)
if n not in d.keys():
    print("Not Exist, to add?")
    choose=input("yes or no?")
    if choose=="yes":
        d.update({n:n*10})
        print(d)


