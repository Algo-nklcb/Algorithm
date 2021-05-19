from sys import stdin
n = int(stdin.readline())

consults = [None]

for i in range(n):
    days, fee = map(int, stdin.readline().split())
    consults.append({'days':days, 'fee':fee})

dp = [0] * (n + 1)

def isConsult(today, past):
    global consults
    return past + consults[past]['days'] <= today

for today in range(1, n + 1):
    max_dp = 0
    for past in range(1, today):
        if isConsult(today, past):
            max_dp = max(dp[past], max_dp)
    if today + consults[today]['days'] <= n + 1:
        # print(max_dp + consults[today]['fee'], today)
        dp[today] = max_dp + consults[today]['fee']
    else:
        dp[today] = max_dp

print(max(dp))