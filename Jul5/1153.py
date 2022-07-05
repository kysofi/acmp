N = input()
word = []
count = 1
max = 0

for i in N:
    if i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u':
        word += '0'
    else: 
        word += '1'

for i in range (len(word)):
    if i != (len(word)-1):
        if word[i] == word[i+1]:
            count +=1
        else:
            count = 1
        
        if count > max:
            max = count 

if max <= 2:
    print (0)
if max == 3:
    print (1)
if max == 4:
    print (1)
if max == 5:
    print (2)
if max == 6:
    print (2)