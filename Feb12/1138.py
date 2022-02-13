numbers=list(map(int,input().split()))
 
i = 0
maxx = []

while numbers[i] != 0:

    current = numbers[i]
    next = numbers [i+1]

    if next > current:
        maxx = current
    i+=1

print (maxx)

