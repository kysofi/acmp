with open('input.txt') as f:
    lines = f.readlines()

parameters = []
for number in lines[0].split():
    if (number.isdigit()):
        parameters.append(number)

R = int(parameters[0])
C = int(parameters[1])

arr_2d = []

for i in range (R):
    arr_2d.append(lines[i+1].split())

rows_sums = []
sum = 0
# calculating sum of each row
for i in range (R):
    for j in range(C):
        sum += int(arr_2d[i][j])
    rows_sums.append(sum)
    sum=0

columns_sums = []
sum = 0
# calculating sum of each column
for i in range (C):
    for j in range(R):
        sum += int(arr_2d[j][i])
    columns_sums.append(sum)
    sum=0

for i in rows_sums:
    print (i, end =" ")
print()

for i in columns_sums:
    print (i, end =" ")
print()

print()

for i in arr_2d:
    for j in i:
        print (j, end =" ")
    print ()
