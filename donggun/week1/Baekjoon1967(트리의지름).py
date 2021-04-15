import sys
from collections import deque

def solution(start):
   dist = {}
   heap = deque(info[start])
   dist[start], max_node, max_weight = 0, 0, 0

   while heap:
      weight, node = heap.popleft()
      
      dist[node] = weight
      if weight > max_weight:
            max_weight = weight
            max_node = node
      
      for adj_node in info[node]:
            w, n = adj_node
            if n not in dist:
               heap.append((w+weight, n))

   return max_node, max_weight

info = dict()
n = int(sys.stdin.readline())

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