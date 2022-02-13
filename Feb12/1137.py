numbers=list(map(int,input().split()))
 
i = 0
length = 0

while numbers[i] != 0:

    current = numbers[i]
    next = numbers [i+1]

    if next > current:
        length+=1
    
    i+=1

print (length)