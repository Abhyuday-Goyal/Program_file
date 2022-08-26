f = open('emails.txt', 'r')
words = f.read().split()
dict_1 = {}
for word in words:
    if word in dict_1:
        dict_1[word] = dict_1[word]+1
    else:
        dict_1[word] = 1
print(dict_1)
value_max=max(dict_1.values())
for word1 in dict_1:
    if dict_1[word1]==value_max:
        print("the most common word is:", word1)