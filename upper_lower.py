from re import L


def s(string):
    upper = 0 
    lower = 0 
    for i in range(0,l):
        if string[i].isupper() == True:
            upper = upper + 1
        elif string[i].islower() == True:
            lower = lower+1
    print("the number of upper case characters are ", upper)
    print("the number of lower case characters are ", lower)
s1 = str(input("enter a string:"))
l = len(s1)
s(s1)
        