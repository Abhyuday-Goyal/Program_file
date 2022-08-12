#to apply binary search, the list must be sorted. 
#binary search cannot be done on a tuple 
L= input("Enter a list in")
l=len(L)
begin = 0
end=l-1
key=int(input("enter element"))
while begin<=end:
    mid = (begin+end) // 2
    if L[mid] < key:
        begin = mid + 1
    elif L[mid] > key:
        end = mid - 1
    else:
        pos= mid
        break
else:
    pos=-1

if pos==-1:
    print("element not found")
else:
    print("element found at position",pos+1)
