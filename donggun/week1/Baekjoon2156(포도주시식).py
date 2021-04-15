n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

max_juice = [0 for _ in range(n)]

max_juice[0] = arr[0]

if n > 1:
    max_juice[1] = arr[0] + arr[1]

if n > 2:
    max_juice[2] = max(max_juice[1], arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, n):
    max_juice[i] = max(max_juice[i-1], max_juice[i-2] + arr[i], max_juice[i-3] + arr[i-1] + arr[i])

print(max_juice[n-1])