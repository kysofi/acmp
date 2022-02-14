numbers = list(map(int,input().split()))

maxx1 = 0
maxx2 = 0

i=0

while numbers[i] != 0:

    if numbers[i] > maxx1: 
        maxx2 = maxx1
        maxx1 = numbers[i]

    elif numbers[i] > maxx2: 
        maxx2 = numbers[i]

    i+=1
    
print (maxx2)



