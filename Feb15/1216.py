n = int(input())
a = list(map(int,input().split()))
area = list(map(int,input().split()))
 
start = area[0] 
finish = area[1]

maxx = 0
position = 0

for i in range (0, n):
    maxx = a[start]
    position = start

for i in range (start,finish):
    if a[i] > maxx:
        maxx = a[i]
        position = i+1
    elif a[i] == maxx:
        position = i
 
print (maxx, position)

# incorrect