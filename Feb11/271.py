N = int(input())

prev = 1
cur = 1
position = 2

while cur < N:
    next = prev + cur
    prev = cur
    cur = next
    position +=1

if cur == N:
    print (1)
    print (position)

else:
    print (0)