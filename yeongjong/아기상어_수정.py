import sys
from collections import defaultdict, deque

n = int(input())
sea = []
q = deque()             # 상어의 위치
fishes = defaultdict()  # 바다에 있는 물고기 수

for i in range(n):
    status = list(map(int, sys.stdin.readline().strip('\n').split(' ')))
    for j, v in enumerate(status):
        if v != 0 and v!= 9:
            fishes[v] += 1
        if v == 9:
            q.append((i, j))
            status[j] = 0
    sea.append(status)

print(q)
# while q:
#     print(q.pop())