# N cities

N = int(input())

x=0

for i in range (0,N):
    roads = list(map(int,input().split()))

    for n in range (0,N):
        if roads[n] == 1:
            x += 1

x = x//2
print(x)


        
            
