inputs = list(map(int,input().split()))

N = int(inputs[0]) # numbers in this line
A = int(inputs[1]) # first left
B = int(inputs[2]) # first right
C = int(inputs[3]) # second left 
D = int(inputs[4]) # second right 

# 9 2 5 6 9

# 1 2 3 4 5 6 7 8 9 (N=9) => 1
# 2 3 4 5 (A=2, B=5) => 5 4 3 2
# 6 7 8 9 (C=6, D=9) => 9 8 7 6

null = []
first = []
second = []
last = []

for i in range (1, N+1):
    if i < A:
        null.append(i)
    elif i >= A and i <=B:
        first.append(i)
    elif i >= C and i <=D:
        second.append(i)
    else:
        last.append(i)

# null >> [1]
# first >> [2 3 4 5]
# second >> [6 7 8 9]
# last >> []

reversed_first =[]

for j in range (0, len(first)):  
    j = (j+1)*(-1)
    reversed_first.append(first[j])

reversed_second =[]

for k in range (0, len(second)):
    k = (k+1)*(-1)
    reversed_second.append(second[k])
    
array = null + reversed_first + reversed_second + last 

for l in range (0,len(array)):
    print (array[l], end=" ")

# incorrect