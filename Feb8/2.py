N = int(input())

sum = 0

if N > 0 :
    for i in range (1,N+1):
        sum +=i
    print(sum)
else:
    for i in range (N,2):
        sum +=i
    print (sum)

"""
      if n > 0:
            sum(list(range(1, n+1)))
        else:
            sum(list(range(n, 2)))
"""