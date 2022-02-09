N = int(input())
k = 0
stepeni = []

while (2**k <= N):
    s = 2**k
    stepeni.append(s)
    k +=1

for i in stepeni:
    print(i, end=" ") 