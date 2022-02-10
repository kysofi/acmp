split_nums=list(map(int,input().split()))

 
i = 0
k = 0
maxx = 0
 
while split_nums[i] != 0:
    k = split_nums[i]
    if k > maxx:
        maxx = k
    i+=1
 
print(maxx)

