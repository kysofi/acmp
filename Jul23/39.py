n = int(input())
price = list(map(int,input().split()))

i = 0
sum  = 0
while i < n:

    maximum = price [i]

    for j in range (i+1,n):
        if price[j]>maximum:
            maximum = price[j]

    sum += maximum
    i+=1

print(sum)