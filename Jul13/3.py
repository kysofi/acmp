num = input()

if num == '5':
    print (25)

else:
    start = int(num[:-1])
    almost = start*(start+1)
    answer = int(str(almost)+'25')
    print (answer)

