inputs = input()
split_nums = inputs.split()
M1=int(split_nums[0])
M2=int(split_nums[1])
M3=int(split_nums[2])

if M1 >= 94 and M1 <= 727 and M2 >= 94 and M2 <= 727 and M3 >= 94 and M3 <= 727:
    maxx = max(M1,M2,M3)
    print(maxx)
else: 
    print ("Error")