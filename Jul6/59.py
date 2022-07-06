numbers = list(map(int,input().split()))
K = numbers [0]
S = numbers [1]
N = []

while K > 0:
    N.append(K%S)
    K=K//S

mul = 1
sum = 0

for i in N:
    mul *= i

for i in N:
    sum += i

print (mul-sum)