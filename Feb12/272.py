numbers =list(map(int,input().split()))

even =[] # четные
odd = [] # нечетные

for i in range (0, len(numbers)):

    if i==0: 
        odd.append(numbers[i]) 
    elif i%2==0:
        odd.append(numbers[i]) 
    else:
        even.append(numbers[i]) 

sum = max (even) + min (odd)
print(sum)