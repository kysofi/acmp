
address = input()
successful = 0
error = 0

if address[0] != '.' and address[len(address)-1] !='.' and '..' not in address and '...' not in address:
    arr = address.split('.')
    if len(arr) == 4:
        for i in range (len(arr)):
            if int(arr[i]) >= 0 and int(arr[i]) <= 255:
                successful +=1
            else:
                error +=1
    else:
        error +=1
else:
    error +=1

if successful == 4 and error == 0:
    print('Good')
else:
    print ('Bad')