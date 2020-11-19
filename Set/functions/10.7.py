def original (list1):
    set1=set(list1)
    list1=list(set1)
    return list1

k=[]
for i in range (10):
    n=input("enter number: ")
    k+=[n]
print(original(k))

# list1=[1,2,3,4,5,5,5,5]
# set1=set(list1)
# list1=list(set1)
# print(list1)