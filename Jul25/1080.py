N = int(input()) # length of the list
nums = list(map(int,input().split())) # numbers
M = int(input()) # number of operations 
operations = []

for i in range (M):
    operations.append(list(input().split()))

for i in range (M):

    #for j in range (0,10):

    if operations[i][0] == 'get': # this 

        print(nums[((int(operations[i][1])-1))])

        #print('nums',nums)

    elif operations[i][0] == 'update':

        for j in range ((int(operations[i][1])-1),int(operations[i][2])):
            nums[j] = int(operations[i][3])
        #print('nums',nums)

    elif operations[i][0] == 'add':

        for j in range ((int(operations[i][1])-1),int(operations[i][2])):
            nums[j] = int(nums[j]) + int(operations[i][3])
        #print('nums',nums)

    elif operations[i][0] == 'rsq': # this 

        sum = 0
        for j in range ((int(operations[i][1])-1),int(operations[i][2])):
            sum += nums[j]
        print(sum)
        #print('nums',nums)

    elif operations[i][0] == 'rmq': # this 

        minimum = ((int(operations[i][1])-1))
        for j in range ((int(operations[i][1])-1),int(operations[i][2])):
            if nums[j]< minimum:
                minimum=nums[j]
        print(minimum)
        #print('nums',nums)

