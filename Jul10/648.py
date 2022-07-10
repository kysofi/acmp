
N = int(input()) # количество всех карточек
cards = list(map(int,input().split())) 

n = N//2  # количество карточек у каждого игрока

# сортировкой пузырьком получили карточки по возрастанию 
for run in range (0, N-1):
    for j in range (0, N-1-run):
        if cards[j] > cards[j+1]:
            cards[j], cards[j+1] = cards[j+1], cards[j]

shrek = sum(cards[n:])
croupier = sum(cards[:n])
print(shrek-croupier)
