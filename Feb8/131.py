N = int(input())

old_man = 0
person = 0 

for i in range (N):
    x = input()
    V = int(x.split(' ')[0])
    S = int(x.split(' ')[1])

    if V > old_man and S==1 :
        old_man = V
        person = i+1

if person != 0:
    print (person)
else: 
    print (-1)





        
    


