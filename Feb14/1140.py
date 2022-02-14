nums = list(map(int,input().split()))

i=0
sum = 0

while nums[i] + nums[i+1] != 0:
    sum += nums[i]
    i+=1

print (sum)