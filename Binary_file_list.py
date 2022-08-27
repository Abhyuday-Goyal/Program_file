import pickle
f = open('lines.dat', 'wb')
list = [[1,'False Impressions',1000],[2,'The Maze Runner', 980],[3,'Harry Potter', 1200]]
pickle.dump(list,f)
input_book = 