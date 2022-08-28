f = open('a.txt','r')
lines = f.readlines()
words = [ 'i','I']
new_words =[]
for i in lines:
    if i[0] in words:
        new_words.append(i)
f.close()
a = open('new.txt', 'w')
b = a.writelines(new_words)
a.close()
c = open('new.txt', 'r')
d = c.readlines()
c.close()
print('the line removed is')
print(d)

        
    