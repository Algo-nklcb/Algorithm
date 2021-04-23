from collections import deque
import copy

n, m = map(int, input().split(' '))

# 맵, visited 등록
map_org = []
for i in range(n):
    row = input().split(' ')
    map_org.append(list(map(int, row)))

# 바이러스 위치 찾기
v_list = []

for row, i in enumerate(map_org):
    for col, j in enumerate(i):
        if j == 2:
            v_list.append((row, col))

# 0,0 0,1 0,2
# 0,0 0,1 0,3
# ...
# 0,0 0,2 0,1

def wall_up(x, y, map):
    if map[x][y] != 1 and map[x][y] != 2:
        map[x][y] = 1
    
import time
def spread_virus(v_map):
    global v_list
    joy_stick = [(0,1),(1,0),(-1,0),(0,-1)]
    count = 0
    for v_x, v_y in v_list:
        que = deque()
        que.append((v_x, v_y))
        while que:
            v_x, v_y = que.popleft()
            for d_x, d_y in joy_stick:
                new_x, new_y = v_x + d_x, v_y + d_y
                if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                    continue
                if v_map[new_x][new_y] == 0:
                    count += 1
                    v_map[new_x][new_y] = 2
                    que.append((new_x, new_y))
    print(count)
    return count

answer = float('inf')
v_map = copy.deepcopy(map_org)
count = 0
for r in range(n):
    for i in range(m):
        f_x, f_y = r, i
        if not wall_up(f_x, f_y, v_map):
            continue
        count += 1
        for j in range(i+1, m):
            s_x, s_y = r, j
            if not wall_up(s_x, s_y, v_map):
                continue
            count += 1
            for k in range(i+2, m):
                t_x, t_y = r, k
                if not wall_up(t_x, t_y, v_map):
                    continue
                count += 1
                if count == 3:
                    n_virus = spread_virus(v_map)
                    if answer > n_virus:
                        answer = n_virus
                    v_map = copy.deepcopy(map_org)
                    count -= 1
                    print(v_map)
print(answer)


