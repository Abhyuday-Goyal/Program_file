#Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 30000

def showEmployee(name, salary = 3000):
  return name, salary 
a = str(input("Enter employee name"))
b = int(input("Enter the salary of employee"))
showEmployee(a,b)

