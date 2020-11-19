def upnlo (n):
    k=0
    # for i in n:
    #     d = i.upper()
    #     if d==i:
    #         k+=1
    # return k
    for i in n:
        if i.isupper()==True:
            k+=1
    return k


name=input("enter name: ")
print("upper: ",upnlo(name))