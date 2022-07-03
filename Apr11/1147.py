# '0'..'9' – (ASCII-коды: 48-57)
# 'A'..'Z' – заглавные (ASCII-коды: 65-90)
# 'a'..'z' – маленькие (ASCII-коды: 97-122)

#option1

input = input()

if (ord(input) >=65 ) and (ord(input)<91):
    print (input)

elif (ord(input) >=97 ) and (ord(input)<123):
    print(chr(ord(input)-32))

