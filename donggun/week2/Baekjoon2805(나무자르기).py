import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
answer = 0
start, end = 0, max(trees)

while start <= end:
    s = 0
    mid = (start+end) // 2

    s = sum(tree-mid if tree > mid else 0 for tree in trees)

    if s < m:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)