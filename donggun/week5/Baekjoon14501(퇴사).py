N = int(input())

dp = [0 for _ in range(N+2)]
Ti = [0 for _ in range(N+1)]
Pi = [0 for _ in range(N+1)]

for i in range(1, N+1):
    Ti[i], Pi[i] = map(int, input().split())

for i in range(N, 0, -1):
    if (Ti[i] + i-1) <= N:
        dp[i] = max(Pi[i] + dp[Ti[i] + i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[1])