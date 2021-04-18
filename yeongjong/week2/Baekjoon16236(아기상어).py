# import heapq

# def dijkstra(start, graph):
#     heap = [(start,0)]
#     distance = [float('inf')] * len(graph)
#     distance[0] = 0
#     while heap:
#         v, w = heapq.heappop(heap)
#         if distance[v] < w:
#             continue
#         for adj_v in graph[v]:
#             new_w = w + adj_v[1]
#             if distance[adj_v[0]] > new_w:
#                 distance[adj_v[0]] = new_w
#                 heapq.heappush(heap, (adj_v[0], new_w))
#     return distance

# graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
#          [(3, 5), (4, 3)],
#          [(0, 3), (4, 9)],
#          [(0, 10), (4, 2)],
#          [(2, 13), (1, 3)]]
# dijkstra(0, graph)

import sys
import queue
import time
from collections import defaultdict
n = int(input())
graph = []
dp = [[0] * n for _ in range(n)]
q = queue.Queue()
level_shark = 2
number_eaten = 0
number_moved = 0
fishes = defaultdict(int)
isfound = False

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

    p = q.get()
    # print(p, dp, number_eaten, level_shark)
    time.sleep(0.2)
    if graph[p[0]][p[1]] < level_shark and graph[p[0]][p[1]] != 0:
        isFound = True
        # 먹고/ 레벨업
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
        print(p, level_shark)
        print(q.empty(), number_moved)

        for x in graph:
            print(x)

        # 엄마 부르기(먹을수 있는 물고기가 없느냐?)
        mommy = False
        for i in range(1, level_shark):
            if fishes[i] > 0:
                mommy = True
                break

        if mommy is False:
            print(level_shark, number_eaten, fishes)
            print("break")
            break
    

    if 0 <= p[0] - 1 and dp[p[0] - 1][p[1]] is 0:
        if graph[p[0] - 1][p[1]] <= level_shark:
            # print("up")
            q.put((p[0] - 1, p[1])) # up
            dp[p[0] - 1][p[1]] = dp[p[0]][p[1]] + 1
    if 0 <= p[1] - 1 and dp[p[0]][p[1] - 1] is 0:
        if graph[p[0]][p[1] - 1] <= level_shark:
            # print("left")
            q.put((p[0], p[1] - 1)) # left
            dp[p[0]][p[1] - 1] = dp[p[0]][p[1]] + 1
    if p[1] + 1 < n and dp[p[0]][p[1] + 1] is 0:
        if graph[p[0]][p[1] + 1] <= level_shark:
            # print("right")
            q.put((p[0], p[1] + 1)) # right
            dp[p[0]][p[1] + 1] = dp[p[0]][p[1]] + 1
    if p[0] + 1 < n and dp[p[0 + 1]][p[1]] is 0:
        if graph[p[0] + 1][p[1]] <= level_shark:
            # print("down")
            q.put((p[0] + 1, p[1])) # down
            dp[p[0] + 1][p[1]] = dp[p[0]][p[1]] + 1
    # print(q.empty())

print(number_moved)
print(dp)
# print(graph)
# print(p_shark)
