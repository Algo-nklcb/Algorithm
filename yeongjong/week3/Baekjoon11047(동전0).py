import sys
from collections import defaultdict
n, m = map(int,sys.stdin.readline().split())


d = defaultdict()
answer = 0
for i in range(n+m):
    p = input()
    if p in d:
        print(p)
    else:
        answer += 1
        d[p] = 1
        
