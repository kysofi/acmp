import random

N = int(input())
A,B,C = list(map(int,input().split()))

# CAPITAL LETTERS 

i=0
capital = []

while i < A:

    new = chr(random.randint(65, 90))

    if i == 0:
        capital.append(new)
        i+=1
    else:
        if new != capital[i-1]:
            capital.append(new)
            i+=1
        else:
            i=i
    
# SMALL LETTERS 

j=0
small = []

while j < B:

    new = chr(random.randint(97, 122))

    if j == 0:
        small.append(new)
        j+=1 
    else:
        if new != small[j-1]:
            small.append(new)
            j+=1 
        else:
            j=j
        
# NUMBERS

k=0
numbers = []

while k < C:

    new = chr(random.randint(48, 57))

    if k == 0:
        numbers.append(new)
        k+=1  
    else:
        if new != numbers[k-1]:
            numbers.append(new)
            k+=1
        else:
            k=k
    
# IF N > A+B+C

m=0
rest = N-A-B-C
extra = []

if N > A+B+C:

    while m < rest:
        
        new = chr(random.randint(97, 122))
        
        if m == 0:
            extra.append(new)
            m+=1  
        else:
            if new != extra[m-1]:
                extra.append(new)
                m+=1  
            else:
                m=m

merged = capital+small+numbers+extra 
answer =''
for i in merged:
    answer+=i
print(answer)
