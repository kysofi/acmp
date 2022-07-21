str = input()
answer = 0

if str[0]=='x':

    if str[1] == '+':
        answer = int(str[4])-int(str[2])
    elif str[1] == '-':
        answer = int(str[4]) +int(str[2])

elif str[2]=='x':

    if str[1] == '+':
        answer = int(str[4])-int(str[0])

    elif str[1] == '-':
        answer = int(str[0])- int(str[4])

elif str[4]=='x':

    if str[1] == '+':
        answer = int(str[0])+int(str[2])
    elif str[1] == '-':
        answer = int(str[0])-int(str[2])

print(answer)
