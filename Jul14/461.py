K = int(input())
groups=[]

for i in input().split():
    groups.append(int(i))

half = (K //2 + 1) # более половины общего количества групп

# Bubble Sort

for run in range (0,len(groups)-1):
    for i in range (0,(len(groups)-1)-run):
        if groups[i]>groups[i+1]:
            groups[i],groups[i+1]=groups[i+1],groups[i]

sum = 0
for j in range(half):
    sum += ((groups[j]//2)+1)

print(sum)