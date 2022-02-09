N = int(input())

x = 2
d = []

while x <= N:
    if N % x == 0:
        d.append(x)
    x+=1

print (min(d))


