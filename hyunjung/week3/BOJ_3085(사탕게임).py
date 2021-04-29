n = int(input())
candy = [[] for _ in range(n)]
answer = 0

for i in range(n):
    candy[i] = list(input())


def checkRow(i):
    max_cnt = 1
    cnt = 1
    curr = candy[i][0]
    for k in range(1, n):
        if curr == candy[i][k]:
            cnt += 1
        else:
            cnt = 1
        curr = candy[i][k]
        max_cnt = max(max_cnt, cnt)
    return max_cnt


def checkCol(j):
    max_cnt = 1
    cnt = 1
    curr = candy[0][j]
    for k in range(1, n):
        if curr == candy[k][j]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
        curr = candy[k][j]
    return max_cnt


def print_candy(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


for i in range(n):
    for j in range(n):
        swapped = False
        if j+1 < n and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            swapped = True

        answer = max(answer, checkRow(i), checkCol(j))

        if swapped:
            answer = max(answer, checkCol(j+1))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            swapped = False

        if i+1 < n and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            swapped = True

        answer = max(answer, checkRow(i), checkCol(j))

        if swapped:
            answer = max(answer, checkRow(i+1))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            swapped = False

print(answer)
