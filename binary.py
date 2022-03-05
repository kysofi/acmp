array = [1,2,3,4,5]
x = 6

left = 0
right = len(array)-1

while right >= left:
    mid = (left + right)//2

    if x == array[mid]:
        print(mid)
        break

    elif x >= array[mid]:
        left = mid+1

    else:
        right = mid-1
        
    return -1