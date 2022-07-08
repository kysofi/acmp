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


prime_numbers = []
nums = list(map(int,input().split()))

for num in nums:
    if is_prime(num):
        prime_numbers.append(num)

sum = sum(prime_numbers)
answer = ''

if is_prime(sum):
    answer = 'Yes'
else: 
    answer ='No'

print (sum)
print (answer)