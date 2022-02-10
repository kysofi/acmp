inputs = input()
split_nums = inputs.split()

x = int(split_nums[0]) # deposit
p = int(split_nums[1]) # persentage
y = int(split_nums[2]) # goal

k = 0

x = x * 100 # в копейках
y = y * 100 # в копейках

p = p + 100 # 20% + 100% = 120% >> //100

while x < y:
    x = (x * p) / 100
    k +=1

print (k)