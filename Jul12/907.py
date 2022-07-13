nums = list(map(int,input().split()))
W = nums[0] # width
H = nums[1] # height
R = nums[2] # radius 

if W >= 2*R and H >= 2*R:
    print ('YES')
else:
    print ('NO')
