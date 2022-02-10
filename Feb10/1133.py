split_nums=list(map(int,input().split()))

i = 0
sum =0

while split_nums[i] != 0:
    sum += split_nums[i]
    i += 1

print(sum)