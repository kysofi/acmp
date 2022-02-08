
input = list(map(int,input().split()))
s = input[0]
p = input[1]

# nested for loops

for x in range (1,1001):
    for y in range (1,1001):
        
        if x + y == s and x * y == p:
            
            if x > y:
                break
                print (y,x)
            else: 
                print (x,y)
            
            break
    
