N = int(input()) 
temperature = input().split()

def quicksort(list):

    less = []
    equal = []
    greater = []
 
    if len (list) > 1:
        pivot = list[0]
        
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
 
        return quicksort(less)+equal+quicksort(greater)
 
    else:
        return list 
 
answer = (quicksort(temperature))

print(*answer)
