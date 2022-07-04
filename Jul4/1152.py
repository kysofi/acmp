N = input()
length = len(N)

new = ''

for i in range (length):

    if i == len(N) - 1:
        new += N[i]
    else: 
        new += N[i] + chr(35)

print (new)
