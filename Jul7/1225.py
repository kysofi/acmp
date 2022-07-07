symbols = list(input().split())

def is_digit(i):
    if ord(str(i)) >= ord('0') and ord(str(i)) <= ord('9'):
        result = 1
    else:
        result = 0
    return result 


answer = 0
for i in symbols:
    answer += is_digit(i)

print (answer)