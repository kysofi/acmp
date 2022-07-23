N = int(input()) 
arr = list(map(int,input().split()))
l,r = list(map(int,input().split()))

max = arr[l-1]
k = l-1

for i in range(l-1,r):

    if arr[i] > max:
        max = arr[i]
        k = i
        
print(max,k+1)

