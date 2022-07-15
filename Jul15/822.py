# first solution 

import math

nums = list(map(int,input().split()))
x1 = nums[0]
y1 = nums[1]
x2 = nums[2]
y2 = nums[3]
x3 = nums[4]
y3 = nums[5]

def len(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) # c = ssqrt (a^2+b^2)


a = int(len(x1,y1,x2,y2))
b = int(len(x1,y1,x3,y3))
c = int(len(x3,y3,x2,y2))

p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(round(s,1))

# second solution 

x1, y1, x2, y2, x3, y3 = map(int, input().split())
print(abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2)

