n, k = map(int, input().split(' '))
coin = []
for _ in range(n):
    coin.insert(0, int(input()))

cnt = 0

for c in coin:
    if k == 0:
        break

    if c <= k:
        cnt += k // c
        k -= (k//c)*c

print(cnt)
