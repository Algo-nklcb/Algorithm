info = dict()
dist = dict()

n = int(input())

if n == 1:
    print(0)
else:
    heap = []

    for _ in range(n-1):
        p, c, w = map(int, input().split())
        if p not in info:
            info[p] = []
        if c not in info:
            info[c] = []

        dist[p], dist[c] = float("inf"), float("inf")
        info[p].append((w, c))
        info[c].append((w, p))

    dist[1] = 0
    max_node = 0
    max_weight = 0

    for node in info[1]:
        heap.append(node)

    while heap:
        pop = heap.pop(0)
        weight = pop[0]
        node = pop[1]

        if dist[node] > weight:
            dist[node] = weight
            if weight > max_weight:
                max_weight = weight
                max_node = node
            
            for adj_node in info[node]:
                w, n = adj_node[0], adj_node[1]
                if w+weight < dist[n]:
                    heap.append((w+weight, n))

    for key in dist.keys():
        dist[key] = float('inf')

    dist[max_node] = 0

    for node in info[max_node]:
        heap.append(node)

    while heap:
        pop = heap.pop(0)
        weight = pop[0]
        node = pop[1]

        if dist[node] > weight:
            dist[node] = weight
            if weight > max_weight:
                max_weight = weight
            
            for adj_node in info[node]:
                w, n = adj_node[0], adj_node[1]
                if w+weight < dist[n]:
                    heap.append((w+weight, n))

    print(max_weight)