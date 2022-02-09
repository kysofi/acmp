N = int(input())

while N > 1:

    if N % 2 != 0:
        print ("NO")
        break
    else:
        N = N // 2
        
    if N == 1: 
        print ("YES")
    
