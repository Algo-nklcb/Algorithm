import collections

n = int(input())
stairs = collections.defaultdict(int)
for i in range(1, n+1):
    stairs[i] = int(input())

dp = collections.defaultdict(int)
# dp[i]: i번째 계단을 밟을 때, i까지의 계단에서 얻을 수 있는 최대 점수
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
