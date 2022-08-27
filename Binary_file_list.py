import pickle
f = open('lines.dat', 'wb')
list = [[1,'False Impressions',1000],[2,'The Maze Runner', 980],[3,'Harry Potter', 1200]]
pickle.dump(list,f)
length = len(list)
list2 =[]
input_book = str(input("enter name of book "))
list2.append(input_book)
list2.append(length+1)
list2.append()
