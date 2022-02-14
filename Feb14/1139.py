numbers = list(map(int,input().split()))

maxx = 0
i=0

while numbers [i] !=0:

    if numbers[i] > maxx:
        maxx = numbers[i]
        count = 1

    elif numbers[i] == maxx:
        count +=1

    i+=1

print (count)

