# Зарплата трех сотрудников 
# Разница (высокооплачиваемый - низкооплачиваемый)

inputs = input()
split_nums = list(map(int, inputs.split(' ')))

max = max(split_nums)
min = min(split_nums)

difference = max -  min

print (difference)

# Python change type of whole list to int??