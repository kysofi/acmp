N = input()

count = 0
max = 0

for i in N:
    if i == '0':
        count +=1 
    else: 
        count = 0
    
    if count > max:
        max = count
    
print (max)