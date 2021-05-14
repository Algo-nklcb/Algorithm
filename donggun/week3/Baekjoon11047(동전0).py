a, b = map(int, input().split())

types = []
answer = 0

for _ in range(a):
    types.append(int(input()))

for i in range(a-1, -1, -1):
    if b >= types[i]:
        answer += b // types[i]
        b = b % types[i]
    if b == 0:
        break

print(answer)