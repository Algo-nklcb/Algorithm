n, m = map(int, input().split())

group1 = set()
group2 = set()

for i in range(n):
    group1.add(input())

for i in range(m):
    group2.add(input())

answer = list(group2.intersection(group1))
answer.sort()

print(len(answer))
for p in answer:
    print(p)


    # if p in group1:
    #     answer += 1

# print(answer)

# group1.sort()
# group2.sort()


# answer = 0
# for p1 in group1:
#     for p2 in group2:
#         if p1 == p2:
#             answer += 1
#             break
# print(answer)

    # l = 0
    # r = m - 1
    # while l <= r:
    #     mid = (l + r) // 2
    #     print(mid)
    #     if p is group2[mid]:
    #         answer += 1
    #         continue
    #     if group2[mid][0] <= p[0]:
    #         r = mid - 1
    #     elif group2[mid][0] > p[0]:
    #         l = mid + 1