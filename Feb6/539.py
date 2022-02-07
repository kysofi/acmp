# ТОРТ

# 2 1, 4 2, 6 3, 8 4 , 10 5, 12 6, 14 7 - четные
# 1 1 , 3 3, 5 3, 7 4, 9 5, 11 6, 13 7 - нечетные

inputs=input()
split_nums=inputs.split(' ')
guests = int(split_nums[0])

if guests % 2 == 0:
    cuts = guests / 2
elif guests == 1:
    cuts = 0
else:
    cuts = guests 

print (int(cuts))