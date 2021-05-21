n, k = map(int, input().split(' '))
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]  # dp[i] = i원을 만들 수 있는 코인의 수

dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[-1])
