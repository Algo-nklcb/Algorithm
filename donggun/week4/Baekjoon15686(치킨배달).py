from itertools import combinations

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
answer = float('inf')

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        if graph[i][j] == 2:
            chickens.append((i, j))

chickens_list = list(combinations(chickens, M))

def distance(chickens):
    global answer
    dist = 0

    for house in houses:
        h_a, h_b = house
        min_dist = float('inf')
        for chicken in chickens:
            c_a, c_b = chicken
            min_dist = min(min_dist, abs(h_a-c_a)+abs(h_b-c_b))

        dist += min_dist
    
    answer = min(answer, dist)

for chickens in chickens_list:
    distance(chickens)

print(answer)