N = int(input()) # количество температур 
nums = list(map(int,input().split()))
temperature = []

for i in range(N):
    temperature.append(nums[i])

# упорядочить по возрастанию 

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len (array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quicksort(less)+equal+quicksort(greater)

    else:
        return array 

answer = (quicksort(temperature))

for x in answer:
    print (x, end=' ')
