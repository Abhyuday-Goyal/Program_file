def unique(l):
  x = [ ]
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique([1,2,3,3,3,3,4,5,6,5,5,2,1,2,3]))