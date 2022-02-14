nums = list(map(int,input().split()))

count = 0
i = 0

while nums[i] !=0:

    if i!=0 and i!=-1:
        if nums[i] > nums[i-1] and nums[i] > nums [i+1]:
            count +=1

    i+=1

print(count)

# no answer