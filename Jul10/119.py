N = int(input())
hours = []
minutes = []
seconds = []
ss =[]

for i in range (N):
    nums = list(map(int, input().split()))
    h = nums[0]
    m = nums[1]
    s = nums [2]

    ss.append(h*3600 + 60*m + s)

# Bubble Sort 

for run in range (N-1):
    for i in range (N-1-run):
        if ss[i]>ss[i+1]:
            ss[i],ss[i+1]=ss[i+1],ss[i]
    
for i in range (N):
    h = ss[i] // 3600
    m = (ss[i] // 60) % 60
    s = ss[i] % 60
    print (h,m,s)