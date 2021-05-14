import heapq


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n
    # 시작노드를 heap에 (자기자신까리 거리 0, 시작 노드) 를 push
    heapq.heappush(heap, (0, start))
    # heap이 빌 때까지
    while heap:
        d, v = heapq.heappop(heap)  # heap에서 pop
        if distances[v] < d:  # 만약 pop한 노드의 거리가 distance[]에 저장된 거리보다 길다면
            continue  # 스킵한다.
        distances[v] = d
        for ad_v in graph[v]:
            if distances[v] + ad_v[1] < distances[ad_v[0]]:
                distances[ad_v[0]] = distances[v]+ad_v[1]
                heapq.heappush(heap, (distances[ad_v[0]], ad_v[0]))

    return distances


n, e = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split(' '))

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split(' '))

start_distance = dijkstra(1, graph)
v1_distance = dijkstra(v1, graph)
v2_distance = dijkstra(v2, graph)

v1_path = start_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = start_distance[v2] + v2_distance[v1] + v1_distance[n]

shortestPath = min(v1_path, v2_path)
if shortestPath < float('inf'):
    print(shortestPath)
else:
    print("-1")
