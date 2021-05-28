from collections import deque

n = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


for i in range(n):
    count = 0
    queue = deque()
    l = int(input())
    start_x, start_y = map(int, input().split())
    queue.append((start_x, start_y))
    end_x, end_y = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    

    while (graph[end_x][end_y] == 0):
        pop_x, pop_y = queue.popleft()
        for i in range(8):
            cur_x, cur_y = pop_x + dx[i], pop_y + dy[i]