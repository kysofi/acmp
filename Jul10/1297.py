def is_prime(num):
    if num == 2:
        return True
    if num > 1: 
        for i in range(2,num):
            if (num%i) == 0:
                return False
    else:
        return False
    return True

input = list(map(int,input().split()))
M = input[0]
N = input[1]

output=[]

for num in range (M,N+1):
    if is_prime(num):
        output.append(num)

if not output:
    print('Absent')
else:
    for i in output:
        print(i, end='\n')
