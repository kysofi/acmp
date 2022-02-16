# can be solved by resolve()

n = int(input())
numbers = list(map(int,input().split()))

for i in range (0,n):
    i = (i + 1) * (-1)
    print (numbers[i], end = " ")

