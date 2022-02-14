nums = list(map(int,input().split()))

i=0
count = 1
maxx = 0

while nums[i] !=0:

    if nums[i]== nums[i+1]:
        count +=1

    else: 
        count = 1
    
    if count > maxx:
        maxx = count

    i+=1

print (maxx)
