import itertools

n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(input())


removed_overlap = set()

for cards in itertools.permutations(cards, k):
    removed_overlap.add(''.join(cards))
print(len(removed_overlap))
