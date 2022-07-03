array1 = [1,1,1,1]
array2 = [2,2,2,2]
array3 = []

for i in range (len(array1)):
        sum = array1[i] + array2[i]
        array3.append(sum)

# print (array3)

array4 = [[1,1,1], [1,1,1]]
array5 = [[2,2,2], [2,2,2]]
array6 = []

for i in range (len(array4)):
    interm = []
    for j in range(len(array4[0])):
        interm.append(array4[i][j]+array5[i][j])
    array6.append(interm)
print(array6)



