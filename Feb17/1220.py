n = int(input())
nums = list(map(int,input().split()))
k = int(input()) # positiv and negativ 


""" 
if k > 0:
    nums = nums [-k:] + nums [:-k]

if k < 0:
    nums = nums [k+1:] + nums [:k+1] 

for num in nums:
    print (num, end = " ")
    
    # incorrect 
"""
"""
# Time limit exceeded

if k < 0:
    for i in range(abs(k)):
        nums.append(nums.pop(0))

else:
    for i in range (k):
        nums.insert(0, nums.pop())

for num in nums:
    print (num, end = ' ')

"""