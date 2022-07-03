input = input()

difference = ord('a') - ord('A')

if (ord(input)) >= 60 and (ord(input)) <= 90:
    print(chr(ord(input)+difference))

if (ord(input)) >= 97 and (ord(input)) <= 122:
    print(chr(ord(input)-difference))

if (ord(input)) >= 33 and (ord(input)) < 60:
    print(input)

if (ord(input)) > 122 and (ord(input)) <= 127:
    print(input)


