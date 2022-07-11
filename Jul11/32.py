a = int(input())
b = int(input())

def is_negative(num):
    if num < 0:
        return True
    else:
        return False

# We need the maximum outcome for (spending - income)
 
# Spending should be the highest if positive and lowest if negative

if is_negative(a):
    spending = list(map(int, str(a)))

else:
    for i in range (len(a)):
        spending.append (int(a[i]))

print (spending)

""" 

# If positive 
# Bubble Sort (DESC)
for run in range (len(spending)-1):
    for i in range (len(spending)-1-run):
        if  spending[i+1] > spending[i]:
            spending[i], spending[i+1] = spending[i+1],spending[i]
        

# Income should be the lowest if positive or the highest if negative
income = []
for i in range (len(b)):
    income.append (int(b[i]))

print (income)

"""