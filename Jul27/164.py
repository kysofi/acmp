nums = input()
ticket = []

for i in range (len(nums)):
    ticket.append(int(nums[i]))

# function to calculate sum and make it from 0 to 9

def summary(number):
    while len(str(number)) != 1:
        n = []
        for i in range (len(str(number))):
            n.append(int(number[i]))
        number = str(sum(n))
    return number

lucky = 0 # lucky number of equal sums

if len(ticket) >1:
    
    for i in range (1,len(ticket)):
        a = ticket[:i]
        b = ticket[i:]
        
        sum_a = str(sum(a))
        sum_b = str(sum(b))
        
        # if summary is not from 0 to 9, use the function and return the correct summary

        if len(sum_a)>1:
            sum_a = summary(sum_a)
        if len(sum_b)>1:
            sum_b = summary(sum_b)
            
        if sum_a == sum_b:
            lucky +=1 
        else:
            lucky +=0

if lucky > 0:
    print('YES')
else:
    print('NO')