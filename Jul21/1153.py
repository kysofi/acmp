word = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
v=0
c=0
sum=0

for i in word:
    if i in vowels:
        v+=1
        c=0
    else:
        c+=1
        v=0
    if v==3:
        sum+=1
        v=1
    elif c==3:
        sum+=1
        c=1

print(sum)
