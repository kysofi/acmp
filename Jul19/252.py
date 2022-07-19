import random
N = int(input())

mass = ''
array = []

for i in range (N):
    mass = input().split()
    array.append(mass)

converted = 0

def convert(number, mass):
    if mass == 'g':
        return int(int(number)) * 1000
    elif mass == 'p':
        return int(number) * 16380 * 1000
    elif mass == 't':
        return int(number) * (1000000) * 1000
    elif mass == 'mp':
        return int(number) * (0.001)*(16380) * 1000
    elif mass == 'kp':
        return int(number) * (1000)*(16380) * 1000
    elif mass == 'Mp':
        return int(number) * (1000000)*(16380) * 1000
    elif mass == 'Gp':
        return int(number) * (1000000000)*(16380) * 1000
    elif mass == 'mg':
        return int(number) # всё переводит в миллиграммы
    elif mass == 'kg':
        return int(number) * (1000) * 1000
    elif mass == 'Mg':
        return int(number) * (1000000) * 1000
    elif mass == 'Gg':
        return int(number) * (1000000000) * 1000
    elif mass == 'mt':
        return int(number) * (0.001) * (1000000) * 1000
    elif mass == 'kt':
        return int(number) * (1000) * (1000000) * 1000
    elif mass == 'Mt':
        return int(number) * (1000000) * (1000000) * 1000
    elif mass == 'Gt':
        return int(number) * (1000000000) * (1000000) * 1000

for i in range (N):
    array[i].append(convert(array[i][0],array[i][1]))

#print(array)

# We need a stable sorting algorithm 
# Counting, Merge or Bubble Sort

# Bubble Sort
""" 
for run in range (N-1):
    for i in range (N-1-run):
        if array[i][2]>array[i+1][2]:
            array[i], array[i+1] = array[i+1], array[i]

for j in range (N):
    print(array[j][0],array[j][1])
"""

# Merge Sort 

def merge_sort(lst):
    if len(lst)<=1:
        return lst 
    middle = len(lst)//2
    left_list = lst[:middle]
    right_list = lst[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return(merge(left_list,right_list))

def merge(left_half,right_half):
    res = []
    while len(left_half)!=0 and len(right_half)!=0:
        if left_half[0][2]<right_half[0][2]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    if len(left_half)==0:
        res += right_half
    else: 
        res += left_half
    return res

#result = (merge_sort(array))
#print(result)

#for i in range(N):
    #print(result[i][0],result[i][1])
