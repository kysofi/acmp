# Fibonacci number
"""
N = int(input())

fibonacci =[0] * (N+1)

fibonacci[0] = 0
fibonacci[1] = 1

k = 2

while k <= (N):
    fibonacci[k]=fibonacci[k-1]+fibonacci[k-2]
    k += 1

print (fibonacci[N])
"""
# RUNTIME ERROR

"""
N = int(input())

a,b = 0,1

for i in range (N):
    a, b = b, a+b
print (a)

"""


