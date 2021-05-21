N, S = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]

start = 0
end = 1
answer = 100001

while start < N:
    if dp[end] - dp[start] >= S:
        if end - start < answer:
            answer = end-start
            if answer == 1:
                break
        start += 1
    
    else:
        if end < N:
            end += 1
        else:
            start += 1
    
if answer != 100001:
    print(answer)
else:
    print(0)