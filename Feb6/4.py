# Игра
# xyz: z-x > 1
# 487, 784, 784 - 487 = 297 (2?)
# x9y, y = 9-x

# K = первая цифра при вычитании 
#  K , 9 , 9 - K

inputs = input()
split_nums=inputs.split(' ')

K = int(split_nums[0])
T = 9
O = T - K

list = [K,T,O]
str = ''.join(map(str,list))

print (str)