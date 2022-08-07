L = eval(input("enter a list"))
print("the unsorted list is",L)
l=len(L)
for i in range(1,l):
    key=L[i]
    j=i-1
    while j>=0 and key>L[j]:
        L[j+1]=L[j]
        j=j-1
    else:
        L[j+1]=key
print("sorted list is", L)
