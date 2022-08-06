L=[1,5,3,9,2,4]
x=int(input("enter element to be serched"))
for i in range(0,len(L)):
    if x==L[i]:
        pos=i+1
        print("element found at position", pos)
        break
else:
    print("element not found")
