'''
split_nums=list(map(int,input().split()))

k = 0

for i in range(len(split_nums)):
    if split_nums[i] != 0:
        k+=1
    else:
        break
print(k)
'''

split_nums=list(map(int,input().split()))

k=0
i = 0

while split_nums[i] != 0:
    k +=1
    i += 1

print (k)