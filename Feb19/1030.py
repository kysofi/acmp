from math import sqrt, trunc

inputs = list(map(int,input().split()))
a1 = int(inputs[0])
a2 = int(inputs[1])
a3 = int(inputs[2])
a4 = int(inputs[3])

# min (a1,a2) + min (a3, a4) - number of cubes
s = trunc(sqrt(min(a1,a2) + min(a3, a4)))

left = 0
right = 2000 * 1000 * 1000

while (left + 1) < right:
    mid = (left+right) //2
    if (mid*mid <=s):
        left = mid
    else:
        right = mid
    
print (left)
