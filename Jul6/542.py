M = int(input())

# перевод в двоичную
dva = []

while M > 0:
    dva.append(M%2)
    M = M//2

# получили уже перевернутую

# из array в число и в строку 

digit=int(''.join(map(str, dva)))
digit = str(digit)

# перевод в десятичную 

answer = 0

for i in range (0,len(digit)):
    answer = answer + int(digit[i])*(2**(len(digit)-i-1)) # 2^

print(answer)