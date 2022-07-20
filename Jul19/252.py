import random
N = int(input())

mass = ''
array = []

for i in range (N):
    mass = input().split()
    array.append(mass)

def convert(number, mass):

    if len(mass)==1:

        if mass== "g":
            number= int(number) * (10 ** 3)
        if mass == "p":
            number = int(number) * 16380 * (10 ** 3)
        if mass == "t":
            number= int(number) * (10 ** 6) * (10 ** 3) 
            
        return number

    if len(mass)==2:

        if mass[1] == "g":

            if mass[0] == "m":
                number= int(number)
            if mass[0] == "k":
                number= int(number) * (10 ** 3) * (10 ** 3)
            if mass[0] == "M":
                number= int(number) * (10 ** 6) * (10 ** 3)
            if mass[0] == "G":
                number= int(number) * (10 ** 9) * (10 ** 3)

        if mass[1]== "p":

            if mass[0] == "m":
                number= int(number) * 16380
            if mass[0] == "k":
                number= int(number) * (10 ** 3) * 16380 * (10 ** 3)
            if mass[0] == "M":
                number= int(number) * (10 ** 6) * 16380 * (10 ** 3)
            if mass[0] == "G":
                number= int(number) * (10 ** 9) * 16380 * (10 ** 3)

        if mass[1] == "t":

            if mass[0] == "m":
                number= int(number) * (10 ** 6)
            if mass[0] == "k":
                number= int(number) * (10 ** 3) * (10 ** 6) * (10 ** 3)
            if mass[0] == "M":
                number= int(number) * (10 ** 6) * (10 ** 6) * (10 ** 3)
            if mass[0] == "G":
                number= int(number) * (10 ** 9) * (10 ** 6) * (10 ** 3)
        
        return number

for i in range (N):
    array[i].append(convert(array[i][0],array[i][1]))

# We need a stable sorting algorithm 
# Counting, Merge or Bubble Sort

# Merge Sort 
""" 
def msort(x):
    if len(x) < 2:
        return x

    result = []

    mid = int(len(x) / 2)
    left = msort(x[:mid])
    right = msort(x[mid:])

    while (len(left) > 0) and (len(right) > 0):
        if int(left[0][2]) > int(right[0][2]):
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    result += left
    result += right
    return result

answer = msort(array)
"""

# Quick Sort 

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array)>1:
        pivot = random.choice(array)

        for x in array:
            if x[2]< pivot[2]:
                less.append(x)
            elif x[2]==pivot[2]:
                equal.append(x)
            elif x[2]> pivot[2]:
                greater.append(x)
        
        return quicksort(less)+equal+quicksort(greater)

    else:
        return array

answer = quicksort(array)

for i in range(N):
    print(answer[i][0], answer[i][1])
