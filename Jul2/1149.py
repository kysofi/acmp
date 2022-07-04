N = input()

unicode = (ord('0')) 
count = 0

for i in range (len(N)):
    if ord(N[i]) == unicode:
        count +=1 
        
print (count) 