nums = list(map(int,input().split()))
l = nums[0]
k = nums[1]
n = nums[2]

possibility=0

if l+k == n:
    possibility +=1
elif l+n == k:
    possibility +=1
elif k+n == l:
    possibility +=1

if possibility != 0:
    print('YES')
elif possibility == 0:
    print('NO')
    










