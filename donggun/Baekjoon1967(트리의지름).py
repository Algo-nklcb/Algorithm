import sys

info = dict()
n = int(sys.stdin.readline())

def solution(start):
    global info
    dist = {}
    heap = []
    for key in info.keys():
        dist[key] = float('inf')

    dist[start] = 0
    max_node = 0
    max_weight = 0

    for node in info[start]:
        heap.append(node)

    while heap:
        weight, node = heap.pop(0)

        if dist[node] > weight:
            dist[node] = weight
            if weight > max_weight:
                max_weight = weight
                max_node = node
            
            for adj_node in info[node]:
                w, n = adj_node
                if w+weight < dist[n]:
                    heap.append((w+weight, n))

    return max_node, max_weight

if n == 1:
    print(0)

else:
    for _ in range(n-1):
        p, c, w = map(int, sys.stdin.readline().split())
        if p not in info:
            info[p] = []
        if c not in info:
            info[c] = []

        info[p].append((w, c))
        info[c].append((w, p))

    end_n, end_w = solution(1)
    print(solution(end_n)[1])