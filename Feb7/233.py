from re import L


N = int(input())
B = [1] * N # List of N values
var = 0

for i in range (N):
    B[i] = int(input())
    
for i in range (N):
    if B[i] <= 437:
        print ("Crash", int(i+1))
        var = 1
        break

if var == 0:
    print ("No crash")