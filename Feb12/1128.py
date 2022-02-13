inputs = input()
split_nums = inputs.split(" ")

first = float(split_nums[0])
last = float(split_nums[1]) 

count = 1
EPS = 1e-9
while first < last - EPS:
    first = first * 1.15
    count +=1

print(count)

