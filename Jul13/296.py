num = int(input())

kot  = 0
lisa = 0

# платить трехрублёвыми пока не будет сумма которая делится на 5 на цело 

while num%5 !=0:
    num -=3 
    lisa +=1

kot = num //5 

print (kot, lisa)