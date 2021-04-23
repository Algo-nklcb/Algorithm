from collections import deque
import copy, sys

sys.setrecursionlimit(10**6)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cur_x, cur_y = 0, 0

# 첫 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            cur_x = i
            cur_y = j
            break

level = 2
exp = 0
result = 0

def find():
    global level, cur_x, cur_y, result, exp

    copy_graph = copy.deepcopy(graph)
    copy_graph[cur_x][cur_y] = 0
    visited = []
    queue = deque()
    queue.append((cur_x, cur_y))
    visited.append((cur_x, cur_y))

    while queue:
        tmp_x, tmp_y = queue.popleft()

        # 만약 먹을 수 있는 물고기를 찾은 경우
        if 0 < graph[tmp_x][tmp_y] < level:
            count = copy_graph[tmp_x][tmp_y]

            # 찾은 물고기와 비교
            while queue:
                t_x, t_y = queue.popleft()
                if 0 == graph[t_x][t_y] or graph[t_x][t_y] >= level:
                    continue
                if count >= copy_graph[t_x][t_y]:
                    if tmp_x > t_x:
                        tmp_x, tmp_y = t_x, t_y
                    elif tmp_x == t_x:
                        if tmp_y > t_y:
                            tmp_x, tmp_y = t_x, t_y
                else:
                    break

            result += copy_graph[tmp_x][tmp_y]
            exp, level = (exp+1, level) if exp + 1 < level else (0, level + 1)
            graph[cur_x][cur_y] = 0
            graph[tmp_x][tmp_y] = 0
            cur_x, cur_y = tmp_x, tmp_y
            return find()
            

        for i in range(4):
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]

            # 상어의 범위가 그래프를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 상어의 레벨이 낮아서 갈 수 없는 곳
            if graph[nx][ny] > level:
                continue
            
            # 만약 이동 가능한 공간이고 처음 방문하는 곳이면 좌표 queue에 삽입
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                queue.append((nx, ny))
                copy_graph[nx][ny] = copy_graph[tmp_x][tmp_y] + 1

    return result

print(find())