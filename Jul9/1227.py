numbers = list(map(int,input().split()))

n = numbers[0]
k = numbers [1]
m = (n-k)


def factorial(i):
    result = 1
    for num in range (2, i+1):
        result *= num
    return result

answer = factorial(n)//(factorial(k)*factorial(m))
print(answer)