# 계단 수 입력
n = int(input())

# 각 계단의 점수 기록할 리스트
points = []

# 각 계단의 점수 입력
for _ in range(n):
    points.append(int(input()))

# dp테이블 초기화
max_point = [0 for _ in range(n)]

max_point[0] = points[0]

if n > 1:
    max_point[1] = points[0] + points[1]

if n > 2:
    max_point[2] = max(points[0] + points[2], points[1] + points[2])

for i in range(3, n):
    max_point[i] = max(max_point[i-2] + points[i], max_point[i-3] + points[i-1] + points[i])

print(max_point[n-1])