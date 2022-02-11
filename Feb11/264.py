N = int(input())
temperature = list(map(int,input().split()))

length = 0
maxx=0

for i in range (0, N): 

    if temperature[i] > 0:
        length +=1 

    else:
        length=0

    if length > maxx:
        maxx = length

print(maxx)