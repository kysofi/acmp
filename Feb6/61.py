# Basketball 

inputs1 = input()
inputs2 = input()
inputs3 = input()
inputs4 = input()

split_nums1=inputs1.split(' ')
split_nums2=inputs2.split(' ')
split_nums3=inputs3.split(' ')
split_nums4=inputs4.split(' ')

team1=int(split_nums1[0])+int(split_nums2[0])+int(split_nums3[0])+ int(split_nums4[0])
team2=int(split_nums1[1])+int(split_nums2[1])+int(split_nums3[1])+ int(split_nums4[1])

if team1 > team2:
    print(1)
elif team1 < team2:
    print(2)
else: print ("DRAW")
