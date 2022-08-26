f = open( "a.txt", 'r')
file_contents = f.read()
vowels = 0
upper = 0
lower = 0 
consonants = 0
vowel_list = ['a','e','i','o','u']
for char in file_contents:
  if char.lower() in vowel_list:
    vowels = vowels + 1
  elif char.isalpha():
    consonants +=1 
  if char.islower():
    lower += 1
  if char.isupper():
    upper+= 1 
print(vowels)
print(upper)
print(lower)
print(consonants)
  
  
