# acmp 1702 

n = int(input())
array = list(map(int,(input().split())))

index=[]

maxx = int(max(array))

for i in range (0,len(array)):

    if len(array) > 0:

        if array[i] == maxx:
            index.append(i)

            array[i], array[len(array)-1] = array[len(array)-1], array[i]
        
            array.pop((len(array))-1)
            maxx = int(max(array))
        
print(array)
print(index)
