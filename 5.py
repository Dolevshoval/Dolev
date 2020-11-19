list1 = [i for i in range(20)]
print(list1)
list2 = []
for i in list1:
    if i % 3 == 0:
        list1.remove(i)

print(list1)
