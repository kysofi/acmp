n = int(input())
a = '2.7182818284590452353602875'

if n == 0:
    print(3)
elif n == 25:
    print(a)
else:
    print(a[:n+1] + (str(int(a[n+1]) if int(a[n+2])<5 
    else str(int(a[n+1]) + 1))))

