n1 = int(input("how many Fib numbers would you to see?: "))
list1 = [1, 1]
if n1 == 1:
    print("Fib is: ", 1)
if n1 == 2:
    print("Fib is: ", list1)
else:
    for i in range(n1 + 1):
        if 2 > i > 0:
            continue
        else:
            list1 += [list1[i] + list1[i - 1]]
print("Fib is: ", list1)
