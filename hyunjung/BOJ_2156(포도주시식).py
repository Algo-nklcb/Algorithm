import collections

n = int(input())
wines = collections.defaultdict(int)
for i in range(1, n+1):
    wines[i] = int(input())

dp = collections.defaultdict(int)
# dp[i] = i번째를 마시든 안 마시든, i번째까지의 최대 와인 양
dp[1] = wines[1]
dp[2] = wines[1]+wines[2]
dp[3] = max(wines[1]+wines[3], wines[2]+wines[3], dp[2])


for i in range(4, n+1):
    dp[i] = max(dp[i-2]+wines[i],
                dp[i-3]+wines[i-1] + wines[i])
    dp[i] = max(dp[i], dp[i-1])
print(dp[n])
