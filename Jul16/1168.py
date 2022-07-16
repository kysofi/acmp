counts = list(map(int,input().split()))
N = int(counts[0]) # количество абитуриетов 
M = int(counts[1]) # количество абитуриентов, которые будут зачислены
A = []
for i in range (N):
    A.append(input().split())

sum = 0

for i in range (N):
    sum = int(A[i][1])+int(A[i][2])+int(A[i][3])
    A[i].append(sum)

for run in range (N-1):
    for j in range (0,N-1-run):
        if A[j+1][4]>A[j][4]:
            A[j],A[j+1]=A[j+1],A[j]

for run in range (N-1):
    for j in range (0,N-1-run):
        if A[j][4]== A[j+1][4]:
            if A[j][0]< A[j+1][0]:
                A[j],A[j+1]=A[j+1],A[j]

last_winner = []
for i in range (M):
    last_winner = A[i]

print(last_winner[0],last_winner[4])

