with open('input.txt') as f:
    lines = f.readlines()

parameters = []
for number in lines[0].split():
    if (number.isdigit()):
        parameters.append(number)

R = int(parameters[0])

#print(R,C)

arr_2d = []

for i in range (R):
    arr_2d.append(lines[i+1].split())

#print(arr_2d)

# 1st option

""" transposed = [[arr_2d[i][j] for i in range(R)] for j in range(C)]
print (transposed) """

# 2nd option

transposed = [None]*R
for i in range (R):
    transposed[i]=[None]*R
    for j in range (R):
        transposed[i][j]=arr_2d[j][i]

# print(transposed)

for i in transposed:
    for j in i:
        print (j, end =" ")
    print ()