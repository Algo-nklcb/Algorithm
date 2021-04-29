n, m = map(int, input().split(' '))

sum_range = []
nums = [0] + list(map(int, input().split(' ')))

for _ in range(m):
    i, j = map(int, input().split(' '))
    sum_range.append((i, j))

# dp[i] 는 0부터 i번째까지의 합
dp = [0 for i in range(n+1)]

dp[0] = 0
dp[1] = nums[0]
for i in range(1, n+1):
    dp[i] = dp[i-1]+nums[i]

for i in range(m):
    print(dp[sum_range[i][1]]-dp[sum_range[i][0]-1])
