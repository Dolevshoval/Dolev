def xder (n):
    end=1
    for i in n:
        end*=i
    return end

lst=[1,2,3,4,5]
print(xder(lst))