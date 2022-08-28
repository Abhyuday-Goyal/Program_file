f = open("a.txt", "r")
l = f.readlines()
for i in l:
  w = i.split()
  for w1 in w:
    print( w1+'#', end = " ")
    print(" ")