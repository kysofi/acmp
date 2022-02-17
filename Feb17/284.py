n = int(input()) 
nums = list(map(int,input().split())) 

m = int(input()) 

left = 0
right = 0

for i in range (0,m):
    new = list(map(int,input().split()))
    left = new[0]
    right = new[1]

    for j in range (left,right+1):
        print (nums[j-1], end=" ")
    print()