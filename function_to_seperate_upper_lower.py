def sentence(x):
  l = len(x)
  str1 =''
  str2 =''
  for i in range(0,l):
    if x[i].upper() == True:
      str1 = str1+x[i]
    elif x[i].lower == False:
      str2 = str2+x[i]
  print(str1)
  print(str2)
      
  
a = str(input("enter a string "))
sentence(a)
