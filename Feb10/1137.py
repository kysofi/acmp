split_nums=list(map(int,input().split()))
 
i=0
count =0
 
while split_nums[i+1] > split_nums[i]:
    i+=1
    count+=1
 
print (count)

################## 

split_nums=list(map(int,input().split()))
 
i=0
k=0
count=0
 
while split_nums[i] != 0:
 
    if split_nums[i] > k:
        k = split_nums[i]
        count+=1
    i+=1
         
print(count-1)

######################

split_nums=list(map(int,input().split()))
 
i = 0
k = 0
maxx = 0
 
while split_nums[i] != 0:
    k = split_nums[i]
    if k > maxx:
        maxx = k
    i+=1
 
i -=1

print(split_nums[i])