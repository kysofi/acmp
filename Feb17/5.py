n = int(input()) # 1..100 сколько оценок 
numbers = list(map(int,input().split())) # 1..31 # в какие дни он их получил

three = []
four = []


for i in range (0,n):
    if numbers[i]%2 == 0:
        four.append(numbers[i])
    else:
        three.append(numbers[i])

if len(four)>=len(three):
    answer = "YES"
else: 
    answer = "NO"

print (*three, sep = " ")
print (*four, sep = " ")
print (answer)