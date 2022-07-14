

input()
c = [0]*201

for i in input().split():
    c[int(i)]+=1

ans=[]

for i in range (-100,101):
    for j in range(c[i]):
        ans.append(i)

print(*ans)

# answer

input()
l = [0]*209
for e in input().split():
    l[int(e)]+=1
r=[]
for i in range(-100,101):
    for j in range(l[i]):
        r.append(i)
print(*r)

# easy 

input()
l = list(map(int,input().split()))
print(*sorted(l))
