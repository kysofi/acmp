"""
N,A,B,C,D = list(map(int,input().split()))

arr = []
for i in range (1,N+1):
    arr.append(i)

list1 = []

for i in range (A-1,B):
    list1.append(arr[i])

reversed = list1[::-1]

j=0
for i in range (A-1,B):
    arr[i] = reversed[j]
    j+=1

list2 = []

for k in range (C-1, D):
    list2.append(arr[k])

reversed = list2[::-1]

j = 0
for l in range (C-1,D):
    arr[l] = reversed[j]
    j+=1

print(*arr)

""" 

n,a,b,c,d=map(int,input().split())

list1=[]

for x in range(n+1):
    list1.append(x)

list1[a:b+1]=list1[a:b+1][::-1]
list1[c:d+1]=list1[c:d+1][::-1]

print(*list1[1:])

