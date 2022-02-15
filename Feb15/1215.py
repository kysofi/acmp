N = int(input())
numbers = list(map(int, input().split()))
x = int(input())

closest = x + 2001
mindiff = 2001

for num in numbers:

    if abs(x-num) <= mindiff:

        if abs (x-num) == mindiff:
            closest = min(closest,num)

        else:
            closest = num
            mindiff = abs (x - num)

print (closest)