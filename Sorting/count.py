# Count Sorting
# Time complexity 0(n)

array = [1,2,8,4,2,4,1,6,7,8,9,10,10]
# Output = [1,1,2,2,...] >> sorted array

maxx = int(max(array))
minn = int(min(array))

buckets = {}

# initialize the buckets
for i in range (minn, maxx+1):
    buckets[i] = 0

# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

# add values to buckets (bucketsort)

for l in range (len(array)):
    buckets[array[l]] +=1

 # {1: 2, 2: 2, 3: 0, 4: 2, 5: 0, 6: 1, 7: 1, 8: 2, 9: 1, 10: 2}

# loop through buckets and construct the array answer

sorted_array=[]

for key in buckets:
    for i in range (1, buckets[key]+1):
        sorted_array.append(key)

print (sorted_array)