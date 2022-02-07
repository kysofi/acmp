# Сбор земляники 
# X = Masha 
# Y = Misha 
# Z = Masha and Misha ate 

inputs = input()
split_nums= inputs.split(' ')

X = int(split_nums[0])
Y = int(split_nums[1])
Z = int(split_nums[2])

result = (X + Y) - Z

if (X + Y) >= Z:
    print (result)
else: 
    print("Impossible")



