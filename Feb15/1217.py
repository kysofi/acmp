n = int(input())
scores = list(map(int,input().split()))

# all maxx should become minn 

minn = min(scores)
maxx = max(scores)

for i in range (0,n):
    if scores[i] == maxx:
        scores [i] = minn
    print (scores[i], end =' ')