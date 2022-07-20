import random 

N = int(input())
A,B,C = list(map(int,input().split()))

i=0
j=0
k=0
m=0
rest = 0

capital = []
small = []
numbers = []
extra = []
    
while i < A:
        
        new = chr(random.randint(65, 90))

        if i == 0:
            capital.append(new)

        else:
            if new != capital[i-1]:
                capital.append(new)   

        i+=1

while j < B:
    
        new = chr(random.randint(97, 122))

        if j == 0:
            small.append(new)
            
        else:
            if new != small[j-1]:
                small.append(new)

        j+=1

while k < C:

        new = chr(random.randint(48, 57))
        
        if k == 0:
            numbers.append(new)

        else:
            if new != numbers[k-1]:
                numbers.append(new)
       
        k+=1

if N > A + B + C:
    
    rest = N - A - B - C

    while m < rest:

        new = chr(random.randint(97, 122))
        
        if m == 0:
            extra.append(new)

        else:
            if new != extra[m-1]:
                extra.append(new)


merged = capital+small+numbers+extra

answer = ''

for i in merged:
    answer+=i

print(len(answer))

