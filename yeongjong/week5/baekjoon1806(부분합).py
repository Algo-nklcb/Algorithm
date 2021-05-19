def solution():
    lenX, sum = map(int, input().split())
    x = list(map(int, input().split()))
    start = 0
    end = 0
    temp_sum = 0
    answer = lenX + 1

    while start < lenX:
      if temp_sum < sum and end < lenX: ## 조건 불만족
        temp_sum += x[end]
        end += 1
      else:                             ## 조건 만족
        temp_sum -= x[start]
        start += 1
      if temp_sum >= sum:
        answer = min(end - start, answer)
    if answer == lenX + 1:
      return 0
    return answer
print(solution())
