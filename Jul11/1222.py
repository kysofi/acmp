nums = list(map(int,input().split()))
N = int(nums[0]) # people 
M = int(nums [1]) # requests

phone = []
name = []
address = []

for i in range (N):
    phone.append (input())
    name.append (input())
    address.append (input())

requests = []

for j in range (M):
    requests.append (input())


for i in range(len(requests)):
    for j in range(len(phone)):
        if requests[i] == phone [j]:
            print (f'{name[j]} ({address[j]})')
            