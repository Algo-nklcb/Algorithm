n = int(input())
times = []
prices = []
for _ in range(n):
    t, p = map(int, input().split(' '))
    times.append(t)
    prices.append(p)

dp = [0 for _ in range(n+1)]  # dp[i] = i번째 날까지 일을 했을 때 최대 수익

for i in range(n-1, -1, -1):
    if i + times[i] > n:  # n을 초과하는 경우 수행 불가
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+times[i]]+prices[i], dp[i+1])
print(dp[0])
