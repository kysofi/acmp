N = input()
length = len(N)

count = 0

for i in range (length):
    if N[i] == '0':
        count +=1
    if N[i] == '6':
        count +=1
    if N[i] == '8':
        count +=2
    if N[i] == '9':
        count +=1
print(count)