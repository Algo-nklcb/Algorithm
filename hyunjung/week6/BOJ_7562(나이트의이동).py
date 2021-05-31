from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y, e_x, e_y):
    q = deque()
    q.append([x, y])
    chessboard[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == e_x and y == e_y:
            return chessboard[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if chessboard[nx][ny] == 0:
                    q.append([nx, ny])
                    chessboard[nx][ny] = chessboard[x][y] + 1

t = int(input())
for _ in range(t):
    l = int(input())
    chessboard = [[0]*l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        continue
    print(bfs(x1, y1, x2, y2))