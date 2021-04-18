def solution(n):
    # arithmetic progress
    def is_ap(n):
        n = list(map(int, str(n)))
        return n[0] - n[1] == n[1] - n[2]
    answer = 0
    if n < 100:
        answer = n
    else:
        answer = 99
        for i in range(100, n + 1):
            if is_ap(i):
                answer += 1
    return answer

n = int(input())

print(solution(n))