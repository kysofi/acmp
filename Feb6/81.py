# Арбузы 
# 1 - тёще (самый легкий)
# 2 - себе (самый тяжелый)

# Solution 1 (нельзя массив)
"""N = int(input())
watermelon_weights = list(map(int,input().split()))

maxx = max(watermelon_weights)
minn = min(watermelon_weights)

print(minn,maxx) """

# Solution 2

N = int(input())
weights = list(map(int,input().split()))

minn = weights[0]
maxx = weights[0]

for i in range (0,N):
    if weights[i] < minn:
        minn = weights[i]
    if weights[i] > maxx:
        maxx = weights[i]

print (minn, maxx)

