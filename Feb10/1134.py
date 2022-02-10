split_nums=list(map(int,input().split()))

i = 0
k = 0

while split_nums[i] != 0:
    if split_nums[i] %2 ==0:
        k+=1
    i += 1
print(k)