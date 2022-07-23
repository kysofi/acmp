input = input()
arr = []

for i in input:
    arr.append(i)

if len(arr) !=5 or arr[2] != '-' or arr[0] < 'A' or arr[0] > 'H' or arr[3] <'A' or arr[3] > 'H' or int(arr[1]) <1 or int(arr[1]) > 8 or int(arr[4]) <1 or int(arr[4]) > 8:
    print('ERROR')

elif (abs((ord(arr[0])-ord(arr[3])) * (int(arr[1])-int(arr[4]))) )== 2:
    print('YES')

else: 
    print('NO')
    