N = int(input())

x = 1
output =[]

while (x**2  <= N):
    y = x**2
    output.append(y)
    x+=1

for y in output:
    print(y, end=" ") 
