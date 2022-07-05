# 1st solution

N = int(input()) # N - length
password = ''

M = list(map(int,input().split()))

A = int(M[0]) # ord('A') - ord ('Z') 65-90
B = int(M[1]) # ord('a') - ord ('z') 97-122
C = int(M[2]) # ord('0') - ord ('9') 48-57
 
upper = range(ord('A'), ord('Z'))
for i in range (A):
    password += chr(upper[i])

lower = range(ord('a'), ord('z'))
for i in range (B):
    password += chr(lower[i])

digits = range(ord('0'), ord('9'))
for i in range (C):
    password += chr(digits[i])

print (password)

# 2nd solution

N = int(input()) # N - length
password = ''
 
M = list(map(int,input().split()))
 
A = int(M[0]) # ord('A') - ord ('Z') 65-90
B = int(M[1]) # ord('a') - ord ('z') 97-122
C = int(M[2]) # ord('0') - ord ('9') 48-57
  
for i in range (A):
    password += (chr(ord('A')+i))
 
for j in range (B):
    password += (chr(ord('a')+j))
 
for k in range (C):
    password += (chr(ord('0')+k))
     
print(password)