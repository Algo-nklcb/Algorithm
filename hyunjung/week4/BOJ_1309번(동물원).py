n = int(input())


def calcTmp(a, b, c):
    return a+b+c

# dp[i-2] + dp[i-1]*2 = dp[i]


answer = 0
if n == 1:
    print(calcTmp(1, 1, 1))
else:
    a, b, c = 1, 1, 1
    tmp = calcTmp(a, b, c)

    for i in range(2, n+1):
        answer = (a*3+b*2+c*2)
        a, b, c = tmp, (answer-tmp)//2, (answer-tmp)//2
        tmp = answer

    print(answer % 9901)
