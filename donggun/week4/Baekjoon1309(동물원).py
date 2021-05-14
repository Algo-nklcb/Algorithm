N = int(input())

dp = [1 for _ in range(100001)]

dp[1] = 3

sum = 1

if N > 1:
    for i in range(2, N+1):
        dp[i] = (2 + dp[i-1] + (sum*2)) % 9901
        sum += dp[i-1]

print(dp[N])