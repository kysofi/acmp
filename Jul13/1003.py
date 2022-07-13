nums = list(map(int,input().split()))
X = int(nums[0])
Y = int(nums[1])
Z = int(nums[2])

k = 3
r = 3 + 2
f = r + 7

sum = X * k + Y * r + Z * f
print(sum)