n = int(input())

points = []

for _ in range(n):
    points.append(int(input()))

max_point = [0 for _ in range(n)]

max_point[0] = points[0]

if n > 1:
    max_point[1] = points[0] + points[1]

if n > 2:
    max_point[2] = max(points[0] + points[2], points[1] + points[2])

for i in range(3, n):
    max_point[i] = max(max_point[i-2] + points[i], max_point[i-3] + points[i-1] + points[i])

print(max_point[n-1])