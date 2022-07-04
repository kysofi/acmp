N = input()
new = ''

for i in range (len(N)):
    if N[i] == 'a':
         new += 'z'
    else: 
         new += (chr((ord(N[i]))+1))
print (new)

    