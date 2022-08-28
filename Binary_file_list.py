import pickle
books = [[1,'False Impressions',1000],[2,'The Maze Runner', 980],[3,'Harry Potter', 1200]]
for book in books:
    f = open('lines.dat', "ab")
    pickle.dump(book, f)
    f.close()

input_book = str(input("enter name of book "))
input_price = int(input("Enter price of book"))
f = open('lines.dat','rb+')
book_list = []
while True:
    try:
        book = pickle.load(f)
        book_list.append(book)
    except EOFError:
        break
f.close()

for book in book_list:
    if book[1] == input_book:
        book[2] = input_price
f= open('lines.dat', "wb")
for book in book_list:
    pickle.dump(book,f)
f.close()

#Print out file
f = open('lines.dat','rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()

