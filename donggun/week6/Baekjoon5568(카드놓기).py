from itertools import permutations

n = int(input())
k = int(input())

cards = []

for _ in range(n):
    cards.append(int(input()))

cardsComb = set(permutations(cards, k))
answer = set()

for comb in permutations(cards, k):
    res = ""
    for item in comb:
        res+=str(item)
    answer.add(res)

print(len(answer))