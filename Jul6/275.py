
N = int(input())
answer =[]

for i in range (N):
    M = int(input())
    if M % 7 == 0:
        answer.append('Yes')
    else:
        answer.append('No')

for i in answer:
    print(i, end="\n" ) 
