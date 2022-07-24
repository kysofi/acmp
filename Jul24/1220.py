N = int(input())
nums = list(map(int,input().split()))
K = int(input())

if K == 0: 
    nums = nums

if abs(K)>N:
    if K < 0:
        K = (K%N) * (-1)
    else:
        K = K%N

if K > 0: 
    answer = nums[-K:] + nums[:(N-K)]

if K < 0:
    K = abs(K)
    answer = nums[-(N-K):] + nums[:K]

print(*answer)

""" 
if K > 0: 
    for i in range(K):
        nums.insert(0,nums.pop(-1))
        # pop last, insert to the beginning

if K < 0:
    for i in range(abs(K)):
        nums.append(nums.pop(0))
        # pop first, append to the end
"""
