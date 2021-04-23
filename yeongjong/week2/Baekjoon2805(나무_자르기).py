from sys import stdin
n, m = map(int, stdin.readline().split())

trees = list(map(int, stdin.readline().split()))

max_cutter = 2000000000
min_cutter = 1
answer = 0
while min_cutter <= max_cutter:
    mid = (min_cutter + max_cutter) // 2

    sum_cut_trees = sum(map(lambda t: t - mid if t - mid > 0 else 0, trees))
    if sum_cut_trees < m:
        max_cutter = mid - 1
    else:
        min_cutter = mid + 1
        if answer < mid:
            answer = mid
print(answer)

