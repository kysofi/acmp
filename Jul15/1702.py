# Selection sort using the max value 
""" 
input()
answer = []

def maxsort(A):
    size = len(A)-1 

    for i in range(0,size):
        max_index = 0

        for j in range(0, (size -i)+1):
            if A[j] > A[max_index]:
                max_index = j
                answer.append(j)

        A[size-i], A[max_index] = A[max_index], A[size-i]

A = list(map(int, input().split()))

maxsort(A)
print(*answer)
"""
ans = []
def ssort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[j],lst[i]=lst[i],lst[j]
                ans.append(i)
    return lst

lst=[int(i) for i in input().split()]
print(ssort(lst))
print(*ans)