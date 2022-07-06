numbers = list(map(int,input().split())) 
N = str(numbers[0])
M = str(numbers [1])

first = 0
second = 0

for i in range (0,len(N)):
    first = first + int(N[i])*(3**(len(N)-i-1)) # 3^

for i in range (0,len(M)):
    second = second + int(M[i])*(3**(len(M)-i-1))
    
print(first + second)