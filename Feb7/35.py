# k автоматов
# n состояний
# m переходов
# d интерес для науки 
# d = 19m + (n + 239)*(n + 366) / 2

k = int(input())

for i in range (0,k):
    x = input()
    n = int(x.split(' ')[0])
    m = int(x.split(' ')[1])
    d = 19 * m + (n + 239) * (n + 366) // 2
    print (d)