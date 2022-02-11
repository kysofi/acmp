inputs = input ()
split_nums = inputs.split()

x = int(split_nums[0]) # пробежал в первый день 
y = int(split_nums[1]) # пробежал в последний день

count = 1

while x < y:
    x = x + (x * 15/100)
    count +=1

print (count)

# no asnwer