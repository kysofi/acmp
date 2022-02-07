# Два бандита
# не больше 10 банок 

# H = Harry 
# L = Larry 

inputs = input ()
split_nums = inputs.split(' ')

H = int(split_nums[0])
L = int(split_nums[1])

# кол-во банок = H + L - 1 

sum = H+L-1
non_H = sum - H
non_L = sum - L

print (non_H, non_L )