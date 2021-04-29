"""파이썬 set 활용"""
# n, m = map(int, input().split(' '))
# not_listens = set()
# not_sees = set()

# for i in range(n):
#     not_listens.add(input())

# for i in range(m):
#     not_sees.add(input())

# answer = not_listens & not_sees
# answer = sorted(list(answer))

# print(len(answer))
# for ans in answer:
#     print(ans)

""" 다른 풀이 - 이분탐색 이용"""
n, m = map(int, input().split(' '))
not_listens = []
not_sees = []

for i in range(n):
    not_listens.append(input())

not_listens.sort()
answer = []


def binary_search(name, left, right):
    while left <= right:
        mid = left+(right-left)//2
        if not_listens[mid] == name:
            answer.append(name)
            return
        elif name > not_listens[mid]:
            left = mid+1
        elif name < not_listens[mid]:
            right = mid-1
    return


for i in range(m):
    name = input()
    binary_search(name, 0, n-1)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)
