# 계단의 점화식 생각해보기
# 1. f(n) 은 마지막 계단을 무조건을 포함한다.
# 2. f(n) = 막계 + 막막계 + f(n-3) 혹은 막계 + f(n-2)

# 0번째를 비워두고 n을 1부터 시작하면 n과 계단의 번째를 일치화 할 수 있다.

n = int(input())

scores = [0]
for i in range(n):
    scores.append(int(input()))


if n == 1:
    print(scores[1])
elif n == 2:
    print(scores[1] + scores[2])
elif n == 3:
    print(max(scores[1] + scores[3], scores[2] + scores[3]))
else:
    dp = [0] * len(scores)
    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]
    dp[3] = max(scores[1] + scores[3], scores[2] + scores[3])
    for i in range(4, n + 1):
        f_c = scores[i] + scores[i-1] + dp[i-3]
        s_c = scores[i] + dp[i-2]
        dp[i] = max(f_c, s_c)
    print(dp[n])

