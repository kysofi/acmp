# Bubble sorting >> two loops

N = int(input())
nums = list(map(int,input().split()))

swap = 0

for i in range (0, N-1):
    for j in range (0, N-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swap +=1

print(swap)
