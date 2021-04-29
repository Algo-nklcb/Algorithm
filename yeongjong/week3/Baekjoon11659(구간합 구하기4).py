n, m = map(int,input().split())

l = list(map(int, input().split()))


for _ in range(m):
    f, s = map(int,input().split())
    sum(l[f:s])