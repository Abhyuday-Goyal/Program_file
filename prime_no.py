n=int(input(' enter a number '))
f= False
if n>1:
    for i in range (2, n):
        if n%i==0:
            f = True
            break
if f :
    print(n,"is not a prime number ")
else:
    print(n,'is a prime number')
