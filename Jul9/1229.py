nums = list(map(int, input().split()))
x1 = nums[0] 
y1 = nums[1]
x2 = nums[2]
y2 = nums[3]
x3 = nums[4]
y3 = nums[5]

def side(x1,y1,x2,y2):
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    # (0-0)^2 + (3-0)^2 = 9
    # (5-0)^2 + (0-0)^2 = 25
    # (0-5)^2 + (3-0)^2 = 34

a = side(x1,y1,x2,y2) # 0,3,0,0

b = side(x3,y3,x2,y2) # 5,0,0,0

c = side(x1,y1,x3,y3) # 0,3,5,0


if (a+b ==c or a+c==b or b+c==a):
    print('Yes')
else:
    print ('No')