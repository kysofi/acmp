N = int(input()) # количество температур 
nums = list(map(int,input().split()))
temperature = []

for i in range(N):
    temperature.append(nums[i])

n = 1
while n < N:
   for i in range(N - n):
       if temperature[i] > temperature[i + 1]:
           temperature[i], temperature[i + 1] = temperature[i + 1], temperature[i]
   n += 1


for x in temperature:
    print (x, end=' ')