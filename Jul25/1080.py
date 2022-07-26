N = int(input()) # length of the list
nums = list(map(int,input().split())) # numbers
M = int(input()) # number of operations 

operations = []

for i in range (M):
    operations.append(list(input().split()))

def get(i):  # this
    print(nums[(int(i)-1)])
    return nums

def update(i,j,k):
    for z in range ((int(i)-1),int(j)):
        nums[z] = (int(k))
    return nums

def add(i,j,k):
    for z in range ((int(i)-1),int(j)):
        nums[z] += (int(k))
    return nums

def rsq(i,j): # this
    sum = 0
    for z in range ((int(i)-1),int(j)):
        sum += nums[z] 
    print(sum)
    return nums
    
def rmq(i,j): # this
    minimum = ((int(i)-1))
    for z in range ((int(i)-1),int(j)):
        minimum=min(nums[z],minimum)
    print(minimum)
    return nums
    
for num in range(M):

    if operations[num][0]=='get':
        get(operations[num][1])
    elif operations[num][0]=='update':
        update(operations[num][1],operations[num][2],operations[num][3])
    elif operations[num][0]=='add':
        add(operations[num][1],operations[num][2],operations[num][3])
    elif operations[num][0]=='rsq':
        rsq(operations[num][1],operations[num][2])
    elif operations[num][0]=='rmq':
        rmq(operations[num][1],operations[num][2])
