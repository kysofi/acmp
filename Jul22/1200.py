K = int(input())

# fast solution 

employees = []

for i in range (K): # в каждой строчке запиши фамилии
    row = input().split()[::-1]
    employees.append(row)
    
for i in range (K):
    print(*employees[i])

# Sonya's solution

employees = []
row = []
late = []
 
for i in range (K): # в каждой строчке запиши фамилии
 
    employees.append(input().split())
     
for i in range (K):
 
    row = employees[i]
    new = []
 
    for j in range (len(row)): # в каждой фамилии
        new.append(row[len(row)-1-j])
 
    late.append(new)
 
for i in range (K):
    print(*late[i])