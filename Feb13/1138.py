numbers = list(map(int,input().split()))

maxx1 = 0
maxx2 = 0

i=0
while numbers[i] != 0:
    if numbers[i] > maxx1:
        maxx2 = maxx1
        maxx1 = numbers[i]
    elif numbers[i] > maxx2:
        maxx2 = numbers[i]

    i+=1

print (maxx2)

""" 
for i in range (0, len(numbers)):
    
    if numbers[i] == 0:
        break

    if numbers[i] > maxx1:
        maxx1 = numbers[i]

for i in range (0, len(numbers)):

    if numbers[i] == 0:
        break

    if numbers[i] > maxx2 and numbers[i] < maxx1:
        maxx2 = numbers[i]

print (maxx2)
"""
