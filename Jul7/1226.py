symbols = list(input().split())

def is_letter(i):
    if ord(str(i)) >= ord('a') and ord(str(i)) <= ord('z'):
        result = 1
    elif ord(str(i)) >= ord('A') and ord(str(i)) <= ord('Z'):
        result = 1
    else:
        result = 0
    return result 


answer = 0
for i in symbols:
    answer += is_letter(i)

print (answer)