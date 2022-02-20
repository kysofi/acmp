R = int(input())
L = 1
count = 0

while R > L:
    R = (R+L) // 2
    count +=1

print(count)