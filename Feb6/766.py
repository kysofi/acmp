inputs = input()
split_nums = inputs.split(' ')

N = int(split_nums[0])
M = int(split_nums[1])
K = int(split_nums[2])

if N * M >= K:
    print("YES")
else: 
    print("NO")