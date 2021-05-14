# 진입차수, 진출차수가 중요
# 1. 진입차수가 0인 노드를 q에 삽입
# 2. q에서 노드를 하나씩 pop하며 해당 노드와 연결된 노드의 진입차수를 1개 차감(진출차수가 1개 이상인 경우)
# 2-1. 2번에 의해 방향성조건 만족
# 3. 2번에 의해 진입차수가 0이된 노드는 다시 q에 삽입함
# 4. q에서 pop한 노드에 연결된 노드가 없을 때 까지 반복
# 4-1. 4번은 진출차수가 0인 것을 의미
# 4-2. 4번 조건에 의해 그래프는 반드시 사이클이 없는 방향 그래프(DAG) 여야함.
# 4-3. DAG는 진입차수가 0인 노드가 반드시 존재함.
# 4-4. 모든 노드가 진입차수가 1 이상이라는 말이 각 노드가 진출차수가 1이상이라는 말이되고 이는 DAG가 아님을 의미.

# DAG의 특징 정리
# 1. 진입차수가 0인 노드가 하나이상 존재한다.
# 2. 진출차수가 0인 노드가 하나이상 존재한다.
# 3. 사이클이 없어야 한다.


# 위상정렬의 의미는 단순히 그래프의 방향에 따라 모든 노드를 순서대로 나열하는 것이 아니다.
# A 노드를 바라보는 두개의 B, C노드가 있을 때 이 두 노드를 모두 먼저 나열한 이후에야 A 노드를 나열할 수 있음을 의미한다.


# 진출차수, 집입차수

from collections import deque, defaultdict
from sys import stdin
destination_node, n = map(int, stdin.readline().split())

graph = defaultdict(list)
dictIndegree = defaultdict(int)

for i in range(n):
  node_info = list(map(int, stdin.readline().split()))
  node = node_info[0]
  node_children = node_info[1:]
  graph[node] = node_children
  dictIndegree[node]
  for node in node_children:
    graph[node]
    dictIndegree[node] += 1

que = deque()

for node, indegree in dictIndegree.items():
  if indegree == 0:
    que.append(node)

answer = []
while que:
  current_node = que.popleft()
  answer.append(current_node)
  for child_node in graph[current_node]:
    dictIndegree[child_node] -= 1
    if dictIndegree[child_node] == 0:
      que.append(child_node)

print(answer)








