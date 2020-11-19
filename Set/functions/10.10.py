def palindrom (n):
    if n==n[::-1]:
        return "Palindrom"
    else:
        return "Nor Palindrom"

name=input("Enter name: ")
print(palindrom(name))