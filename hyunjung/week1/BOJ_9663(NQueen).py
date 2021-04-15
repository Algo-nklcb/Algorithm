n = int(input())
chess_board_row = [0 for _ in range(n)]
answer = 0


def dfs(r):
    global answer

    if r == n:
        answer += 1

    else:
        for i in range(n):
            chess_board_row[r] = i
            placed = True
            for j in range(r):
                if chess_board_row[r] == chess_board_row[j] or abs(chess_board_row[r] - chess_board_row[j]) == r - j:
                    placed = False
                    break
            if placed:
                dfs(r + 1)


dfs(0)
print(answer)
