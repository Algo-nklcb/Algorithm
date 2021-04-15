# 접근방식
# 1. 포도주의 잔의 개수가 10000개 이하이기 때문에, 2중포문 불가능
# 2. f(n)은 n번 까지의 포도주를 선택한 경우의 최대양으로 가정
# 3. f(n)과 f(n-1) f(n-2) f(n-3)과의 관계 파악

n = int(input())

wines = []
for i in range(n):
    wines.append(int(input()))

n = len(wines)
if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0] + wines[1])
else:
    dp = [0] * len(wines)
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
    for i in range(3, n):
        f_c = wines[i] + wines[i-1] + dp[i-3]
        s_c = dp[i-1]
        t_c = wines[i] + dp[i-2]
        dp[i] = max(f_c, s_c, t_c)
    print(dp[n-1])