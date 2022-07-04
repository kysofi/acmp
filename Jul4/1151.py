password = input()
length = len (password)
small = 0
large = 0
number = 0
long = 0

for i in range (length):
    if ord(password[i]) >= ord('a')  and ord(password[i]) <= ord('z'):
        small +=1 
    
for i in range (length):
    if ord(password[i]) >= ord('A')  and ord(password[i]) <= ord('Z'):
        large +=1 

for i in range (length):
    if ord(password[i]) >= ord('0')  and ord(password[i]) <= ord('9'):
        number +=1 

if length >= 12:
    long +=1

if small !=0 and large !=0 and number !=0 and long !=0: 
    answer = 'Yes'
    
else:
    answer = 'No'

print (answer)