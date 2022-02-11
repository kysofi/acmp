inputs = input()
split_nums = inputs.split()

x = int(split_nums[0]) # deposit
p = int(split_nums[1]) # persentage
y = int(split_nums[2]) # goal

year = 0

while x < y: 
    x = x + x * (p / 100)
    x = int(100 * x) / 100 # int will get rid of .xxxx 
    
    print(x)
    year +=1

print (year)


