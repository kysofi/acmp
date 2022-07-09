

def happy(n):
    n6 = n % 10
    n5 = n // 10 % 10
    n4 = n // 100 % 10
    n3 = n // 1000 % 10
    n2 = n // 10000 % 10
    n1 = n // 100000 

    return (n1+n2+n3) == (n4+n5+n6)

N = int(input())

for i in range (N):
    a = int(input())
    next = a+1
    last =a-1

    if happy(next) or happy(last):
        print ('Yes')
    else:
        print ('No')

