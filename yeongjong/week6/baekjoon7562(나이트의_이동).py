from sys import stdin
from collections import deque

DISTANCES = (
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
    (-1, -2),
    (-1, 2),
    (-2, -1),
    (-2, 1)
)

n = int(stdin.readline())

def makeBoard(boardSize):
    return [[0]*boardSize for _ in range(boardSize)]

def moveNight(x, y, distance_x, distance_y):
    new_x = x + distance_x
    new_y = y + distance_y
    return new_x, new_y

for _ in range(n):
    boardSize = int(stdin.readline())
    board = makeBoard(boardSize)
    c_x, c_y = map(int,stdin.readline().split()) # current position
    t_x, t_y = map(int,stdin.readline().split()) # target position
    que = deque()
    que.append((c_x, c_y, 0))

    while que:
        c_x, c_y, count = que.popleft()
        if c_x == t_x and c_y == t_y:
            print(count)
            break
        # 이동
        count += 1
        for d_x, d_y in DISTANCES:
            n_x, n_y = moveNight(c_x, c_y, d_x, d_y)
            if 0 <= n_x < boardSize and 0 <= n_y < boardSize:
                if board[n_x][n_y] == 1:
                    continue
                que.append((n_x, n_y, count))
                board[n_x][n_y] = 1