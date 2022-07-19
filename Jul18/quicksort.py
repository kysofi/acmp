import random

a = list(map(int,input().split()))
array = []

for i in range(len(a)):
    array.append (int(a[i]))

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len (array) > 1:

        pivot = random.choice(array)

        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        return quicksort(less)+ equal + quicksort(greater)
    
    else: 
        return array

print (quicksort(array))