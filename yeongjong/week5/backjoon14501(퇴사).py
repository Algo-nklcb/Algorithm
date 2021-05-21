from sys import stdin
n = int(stdin.readline())

consults = [None]

for i in range(n):
    days, fee = map(int, stdin.readline().split())
    consults.append({'days':days, 'fee':fee})

LASTDAY = n + 1

# 날짜별 최대 가능 수입
dp = [0] * (LASTDAY)

# 과거에 시작한 상담이 오늘 기준으로 끝났는가?
def isCompletedPastConsult(today, past):
    global consults
    return past + consults[past]['days'] <= today

# 퇴사일 전까지 상담을 끝마칠 수 있는가?
def isCounsult(today, lastDay):
    global consults
    return today + consults[today]['days'] <= lastDay

for today in range(1, LASTDAY):
    max_dp = 0
    for past in range(1, today):
        if isCompletedPastConsult(today, past):
            max_dp = max(dp[past], max_dp)
    if isCounsult(today, LASTDAY):
        dp[today] = max_dp + consults[today]['fee']
    else:
        dp[today] = max_dp

print(max(dp))