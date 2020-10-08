n = int(input())
cards = []
lost = []

for i in range(1, n+1):
    cards.append(i)

for i in range(0, n-1):
    num = int(input())
    lost.append(num)

for i in lost:
    cards.remove(i)

print(cards[0])
