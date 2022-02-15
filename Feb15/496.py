N = int(input())
numbers = list(map(int,input().split()))

one = 0
two = 0
three = 0

sum = 0 
max_sum = 0

for i in range (0, N):
    one = numbers[i-1]
    two = numbers[i]
    if i == (N-1):
        three = numbers[0]
    else: 
        three = numbers[i+1]
    sum = one + two + three
    if sum > max_sum:
        max_sum = sum

print(max_sum)
    