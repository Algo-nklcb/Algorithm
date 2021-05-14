# 백트래킹
# 반복문 혹은 재귀문에서 코드를 실행할 필요가 없는 경우를 제외시키는 기법
# 보통 메모이제이션을 사용한다.

from sys import stdin
n, m = map(int,stdin.readline().split())

selected_numbers = []
is_used = [False] * n
def pick_number(selected_numbers):
  if len(selected_numbers) == m:
    print(" ".join(selected_numbers))
    return
  for i in range(1, n + 1):
    if is_used[i - 1]:
      continue
    selected_numbers.append(str(i))
    is_used[i - 1] = True
    pick_number(selected_numbers)
    selected_numbers.pop()
    is_used[i - 1] = False
pick_number(selected_numbers)