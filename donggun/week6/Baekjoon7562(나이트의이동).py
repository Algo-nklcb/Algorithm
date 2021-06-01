from collections import deque

cases = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(cases):
    size = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    queue = deque([(start_x, start_y)])
    graph = [[0] * size for _ in range(size)]
    
    while (graph[end_x][end_y] == 0 and not((start_x, start_y) == (end_x, end_y))):
        pop_x, pop_y = queue.popleft()
        for i in range(8):
            moved_x, moved_y = pop_x + dx[i], pop_y + dy[i]
            while (size > moved_x >= 0 and size > moved_y >= 0 and graph[moved_x][moved_y]==0):
                graph[moved_x][moved_y] = graph[pop_x][pop_y] + 1
                queue.append((moved_x, moved_y))
    
    print(graph[end_x][end_y])