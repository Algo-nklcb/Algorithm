v, e = map(int, input().split(' '))
edges = []
for i in range(e):
    v1, v2, w = map(int, input().split(' '))
    edges.append((w, v1, v2))
edges.sort()
mstWeight = 0

parents = [i for i in range(v+1)]  # 본인을 가리킴
rank = [0 for _ in range(v+1)]


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # path compression
    return parents[x]


def union(a, b):
    if rank[a] < rank[b]:  # union-by-rank
        parents[b] = a
    else:
        parents[a] = b

    if rank[a] == rank[b]:
        rank[a] += 1


for edge in edges:
    weight, a, b = edge
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        union(root_a, root_b)
        mstWeight += weight

print(mstWeight)
