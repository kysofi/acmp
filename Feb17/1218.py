n = int(input())
heights = list(map(int,input().split()))
p = int(input())

position = 0

for i in range (0,n):
    if heights[i] >=p:
        position+=1

print(position+1)
