import sys
import queue
from collections import defaultdict

n = int(input())
graph = []
dp = [[0] * n for _ in range(n)]
q = queue.Queue()
level_shark = 2
number_eaten = 0
number_moved = 0
fishes = defaultdict(int)
l = []
for i in range(n):
    status = list(map(int, sys.stdin.readline().strip('\n').split(' ')))
    for j, v in enumerate(status):
        if v != 0 and v!= 9:
            fishes[v] += 1
        if v == 9:
            q.put((i, j))
            status[j] = 0
    graph.append(status)



while not q.empty():
    p = q.get() # 상어 위치
    # 먹을게 발견됐다는 의미
    if graph[p[0]][p[1]] < level_shark and graph[p[0]][p[1]] != 0:
        l_fish = [p]
        # 상어로 부터 같은 거리에 떨어진 물고기중에 가장 위쪽에서 왼쪽에 위치한 물고기 선택
        while not q.empty():
            case = q.get() # 상어 위치
            if  dp[case[0]][case[1]] <= dp[p[0]][p[1]] and graph[case[0]][case[1]] != 0 and graph[case[0]][case[1]] < level_shark:
                l_fish.append(case) # 물고기 후보
        l_fish.sort(key=lambda x: (x[0], x[1]))
        p = l_fish[0]
        number_eaten += 1

        if level_shark == number_eaten:
            level_shark += 1
            number_eaten = 0
        # 먹힌 물고기수 down
        fishes[graph[p[0]][p[1]]] -= 1
        # 먹힌 물고리 자리 0으로 초기화
        graph[p[0]][p[1]] = 0
        # 움직인 거리 추가
        number_moved += dp[p[0]][p[1]]
        # q, dp 초기화
        q.__init__()
        dp = [[0] * n for _ in range(n)]


        # 엄마 부르기(먹을수 있는 물고기가 없느냐?)
        mommy = False
        for i in range(1, level_shark):
            if fishes[i] > 0:
                mommy = True
                break

        if mommy is False:
            break
    

    if 0 <= p[0] - 1 and dp[p[0] - 1][p[1]] is 0:
        if graph[p[0] - 1][p[1]] <= level_shark:
            q.put((p[0] - 1, p[1])) # up
            dp[p[0] - 1][p[1]] = dp[p[0]][p[1]] + 1
    if 0 <= p[1] - 1 and dp[p[0]][p[1] - 1] is 0:
        if graph[p[0]][p[1] - 1] <= level_shark:
            q.put((p[0], p[1] - 1)) # left
            dp[p[0]][p[1] - 1] = dp[p[0]][p[1]] + 1
    if p[1] + 1 < n and dp[p[0]][p[1] + 1] is 0:
        if graph[p[0]][p[1] + 1] <= level_shark:
            q.put((p[0], p[1] + 1)) # right
            dp[p[0]][p[1] + 1] = dp[p[0]][p[1]] + 1
    if p[0] + 1 < n and dp[p[0] + 1][p[1]] is 0:
        if graph[p[0] + 1][p[1]] <= level_shark:
            q.put((p[0] + 1, p[1])) # down
            dp[p[0] + 1][p[1]] = dp[p[0]][p[1]] + 1

print(number_moved)