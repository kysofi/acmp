

N=input()
c = [0]*201

for i in (input().split()):
    c[int(i)]+=1

ans=[]

for i in range (-100,101):
    for j in range(c[i]):
        ans.append(i)

print(*ans)