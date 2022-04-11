#ASCII stands for American Standard Code for Information Interchange

# '0'..'9' – (ASCII-коды: 48-57)
# 'A'..'Z' – заглавные (ASCII-коды: 65-90)
# 'a'..'z' – маленькие (ASCII-коды: 97-122)

input = input()
#digits (48-57)
if (ord(input) >= 48) and (ord(input) < 58):
    print ("Yes")
else: 
    print ("No")

