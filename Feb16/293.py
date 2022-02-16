N = int(input()) # number of companies
V = list(map(int,input().split())) # annual profit per company
P = list(map(int,input().split())) # tax percentage per company 

payment = 0
maxx_payment = 0
company = 0

for i in range(0,N):
    payment = V[i] * P[i]
    payment /=100
    if payment > maxx_payment:
        maxx_payment = payment
        company = i

print(company+1)
    

