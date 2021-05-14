import itertools
import sys


def calcMD(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

# 0-빈칸, 1-집, 2-치킨집


n, m = map(int, input().split(' '))
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([(i, j), n*2+1])  # 최대 거리 2n
        elif city[i][j] == 2:
            chicken.append((i, j))

remainedChicken = list(itertools.combinations(chicken, m))
sum_chickenDistance = sys.maxsize
for rc in remainedChicken:
    for i in range(m):
        rcRow = rc[i][0]
        rcColumn = rc[i][1]
        for h in house:
            h[1] = min(h[1], calcMD(rcRow, rcColumn, h[0][0], h[0][1]))

    tmp_sum_chickenDistance = 0
    for h in house:
        tmp_sum_chickenDistance += h[1]
        h[1] = sys.maxsize
    sum_chickenDistance = min(tmp_sum_chickenDistance, sum_chickenDistance)

print(sum_chickenDistance)
