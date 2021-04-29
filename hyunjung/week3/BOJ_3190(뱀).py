n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

snake_dir = []
for _ in range(k):
    i, j = map(int, input().split(' '))
    board[i][j] = 1
l = int(input())
for _ in range(l):
    t, d = input().split(' ')
    snake_dir.append((int(t), d))

time = 0
r, c = 0, 0
snake = [[0, 0]]
# 1: 위 2:오른쪽 3: 아래 4: 왼쪽
curr_dir = 2  # 뱀은 처음에 오른쪽


def move_snake():
    if curr_dir == 1:
        snake[0][0] += 1

        for idx in range(len(snake)):
            b_i, b_j = snake[i][0], snake[i][1]

            if idx == 0:
                pass
            else:
                pass

            if snake[i][0] >= n or snake[i][1] >= n or board[snake[i][0]][snake[i][1]] == 2:
                return False
            if board[snake[i][0]][snake[i][1]] == 0:
                board[snake[i][0]][snake[i][1]] = 2
                board[b_i][b_j] = 0

    for _ in range(len(snake)):
        i, j = snake.pop(0)
        if i+1 > n or board[i+1][j] == 2:
            return False
        elif board[i+1][j] == 0:
            pass


while True:
    t, d = snake_dir.pop(0)
    if curr_dir == 1:
        for _ in range(t):
            time += 1

            r += 1

    elif curr_dir == 2:
        c += t
    elif curr_dir == 3:
        r -= t
    elif curr_dir == 4:
        c -= t
    if d == 'L':
        curr_dir -= 1
        if curr_dir == 0:
            curr_dir = 4
    elif d == 'R':
        curr_dir += 1
        if curr_dir == 5:
            curr_dir = 1
