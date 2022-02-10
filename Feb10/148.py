inputs = input()
split_nums = inputs.split()

A = int(split_nums[0])
B = int(split_nums[1])

while A != 0 and B != 0:

    if A > B: # 12 > 6
        A = A % B  # 12 % 6 = 0
    else:
        B = B % A # 42 % 12 = 6 

print (A,B)

