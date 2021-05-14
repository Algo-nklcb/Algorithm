import sys

a, b = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(a+1)]

dp[1] = arr[0]

for i in range(2, a+1):
    dp[i] = arr[i-1] + dp[i-1]

for _ in range(b):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[m] - dp[n-1])