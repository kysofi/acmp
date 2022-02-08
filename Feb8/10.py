# A*X^3 + B*X^2 + c*X + D = 0

inputs = input()
split_nums=inputs.split()
A = int(split_nums[0])
B = int(split_nums[1])
C = int(split_nums[2])
D = int(split_nums[3])

answers=[]

for x in range (-100,101):
    if A*(x**3)+B*(x**2)+C*x+D == 0:
        answers.append(x)

for answer in answers:
    print(answer, end=' ')
