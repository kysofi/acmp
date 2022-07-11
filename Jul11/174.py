N = int(input()) # husbands 
inputs = list(map(int,input().split()))
gorgona = int(input())
 
money =[]
for i in range(len(inputs)):
    money.append(int(inputs[i]))

# Bubble Sorting
for run in range(len(money)-1):
    for i in range (len(money)-1-run):
        if money[i]>money[i+1]:
            money[i], money[i+1]=money[i+1],money[i]

for j in range (len(money)):
    gorgona=(gorgona+money[j])/2

print("%.6f" %gorgona)