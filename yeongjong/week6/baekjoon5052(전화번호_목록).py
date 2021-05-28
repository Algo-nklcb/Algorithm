from sys import stdin
input = stdin.readline
cases = int(input())

tri = dict()

for _ in range(cases): # 테스트 케이스
  num = int(input()) # 전화번호 수
  for _ in range(num):
    phoneNumber = int(input())
    for i in phoneNumber:
      current = tri.get(i)
      if current:
        current 