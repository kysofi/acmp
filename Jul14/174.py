N = int(input()) # husbands 
inputs = list(map(int,input().split()))
money =[]

for i in range(N):
    money.append(inputs[i])

gorgona = int(input())

# Bubble Sorting
for run in range(N-1):
    for i in range (N-1-run):
        if money[i]>money[i+1]:
            money[i], money[i+1]=money[i+1],money[i]

for j in range (N):
    gorgona=(gorgona+money[j])/2

print("{0:.6f}".format(gorgona))