# Арифметика
# A B C
# A * B = C => YES
# A * B not C => NO

inputs = input ()
split_nums = inputs.split(' ')

A = int (split_nums[0])
B = int (split_nums[1])
C = int (split_nums[2])

if A*B==C:
    print("YES")
else: 
    print("NO")