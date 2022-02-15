n = int(input()) # number of elements in array
a = list(map(int,input().split())) # array
x = int(input ()) # test_value 

count = 0
for i in a:
    if i == x:
        count +=1

print(count)

""" 
count=0
for i in range (n):
    if a[i]==x:
        count+=1

print (count)

"""