import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

def solution(n):
    for i in range(1, len(s)): # 0~i
        for j in range(i):
            if s[j] < s[i]:
                if (dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
    return dp[n-1]
solution(n)
print(max(dp))

