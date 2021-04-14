import collections

n = int(input())

tree = [collections.defaultdict(int) for i in range(n+1)]
path = [0 for i in range(n+1)]
visited = [False for i in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split(' '))
    tree[p][c] = w

stack = []


def dfs(start, path_length):
    stack.append((start, start, path_length))
    while stack:
        curr, before_node, pl = stack.pop()
        if visited[curr] is False:
            visited[curr] = True
            if tree[curr][before_node] != 0:
                pl += tree[curr][before_node]

            elif tree[before_node][curr] != 0:
                pl += tree[before_node][curr]

            path[curr] = pl

            for adj_v in tree[curr]:
                stack.append((adj_v, curr, pl))


dfs(1, 0)

for i in range(len(visited)):
    visited[i] = False

max_path_length = 0
max_path_node = 0
for idx, p in enumerate(path):
    if max_path_length < p:
        max_path_length = p
        max_path_node = idx

dfs(max_path_node, 0)

print(max(path))
