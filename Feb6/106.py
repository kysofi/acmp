N = int(input())

var = 0

for i in range(0, N):
    var += int(input())

print(min(var,(N-var)))

"""
for i in range(0, N):
    if int(input()) == 1:
        var +=1
    
print(min(var,(N-var)))

for i in range(0, N):
    coin = int(input())
    if coin == 1:
        heads += 1
    else:
        tails +=1

print(min(heads,tails))

i = 0
while i < N:
    coin = int(input())
    coins.append(coin)
    i += 1
"""

