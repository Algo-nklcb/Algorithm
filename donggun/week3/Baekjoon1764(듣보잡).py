n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(input())

for _ in range(m):
    b.append(input())

c = sorted(list(set(a) & set(b)))

print(len(c))
for item in c:
    print(item)