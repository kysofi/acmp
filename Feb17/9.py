N = int(input())
numbers = list(map(int,input().split()))

positiv_sum = 0

for i in range (0,N):
    if numbers[i] > 0:
        positiv_sum = positiv_sum + numbers[i]

minn = min(numbers) # -7
maxx = max(numbers) # 9

boundaries =[]

for i in range (0,N):
    if numbers[i] == minn:
        boundaries.append(i)
    elif numbers[i] == maxx:
        boundaries.append(i)

left_boundary = min(boundaries) # 0
right_boundary = max(boundaries) # 4

multiplication = 1

for i in range (0,N):
    if i >left_boundary and i < right_boundary:
        multiplication = multiplication * numbers[i]

print (positiv_sum, multiplication)