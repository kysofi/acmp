N = int(input())
temperature = list(map(int,input().split()))

length = 0
output=0

for i in range (0, N): 

    if temperature[i] > 0:
        length +=1 

        for j in range(i+1,N):
            
            if temperature[j]>0:
                length +=1

    if length > output:
        output=length

    else:
        break

print (output)

## NO ANSWER