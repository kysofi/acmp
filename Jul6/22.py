N = int(input())
answer = []

while N > 0:
    answer.append(N%2) # остаток от деления 
    N = N//2

print(sum(answer))

