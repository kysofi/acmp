split_nums=list(map(int,input().split()))
 
i=0
while split_nums[i] !=0 and split_nums[i] < split_nums[i+1]:
    i+=1

print (split_nums[i-1])
