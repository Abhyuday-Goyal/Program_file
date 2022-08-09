def args(age, salary):
  if age> 18:
    if salary>30000:
      print("accepted")
    else:
      print("not accepted")
  else:
    print("not accepted")
a = int(input("enter age "))
b = int(input("enter salary"))
args(salary = b, age = a )

