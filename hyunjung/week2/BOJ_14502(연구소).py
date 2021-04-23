import itertools
import copy
n, m = map(int, input().split(' '))
lab = []

for i in range(m):
    lab.append(list(map(int, input().split(' '))))


def dfs(i, j, arr):
    arr[i][j] = 2
    if i+1 < len(arr) and arr[i+1][j] == 0:
        dfs(i+1, j, arr)
    if j+1 < len(arr[0]) and arr[i][j+1] == 0:
        dfs(i, j+1, arr)
    if i-1 >= 0 and arr[i-1][j] == 0:
        dfs(i-1, j, arr)
    if j-1 >= 0 and arr[i][j-1] == 0:
        dfs(i, j-1, arr)
    return


virus = []
notwall = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] != 1:
            notwall.append((i, j))


def count_wall(arr, safe):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                safe += 1
    return safe


three_walls = list(itertools.combinations(notwall, 3))

answer = 0
for w in three_walls:
    tmp_lab = copy.deepcopy(lab)
    tmp_lab[w[0][0]][w[0][1]] = 1
    tmp_lab[w[1][0]][w[1][1]] = 1
    tmp_lab[w[2][0]][w[2][1]] = 1
    for v in virus:
        dfs(v[0], v[1], tmp_lab)
    answer = max(answer, count_wall(tmp_lab, 0))
print(answer)


# print(lab)
