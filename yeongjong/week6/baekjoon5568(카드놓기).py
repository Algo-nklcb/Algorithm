from sys import stdin
from itertools import permutations
n = int(stdin.readline())
k = int(stdin.readline())

deck = []

allCase = set()

for i in range(n):
    deck.append(int(stdin.readline()))

for case in permutations(deck, k):      # case (1,2)
    caseStr = "".join(map(str, case))   # caseStr 12
print(len(allCase))