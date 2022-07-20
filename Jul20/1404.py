A = input()
new = ''

for i in range (len(A)):
    if A[i] == 'z':
         new += 'a'
    else: 
         new += (chr((ord(A[i]))+1))
print (new)

    