n, m = map(int, input().split(' '))

tree = list(map(int, input().split(' ')))
tree.sort(reverse=True)

max_h = max(tree)

answer = 0


def binary_search(s, e):  # s : start, e: end
    global answer
    if s > e:
        return
    mid = s+(e - s)//2
    wood = 0
    for t in tree:
        if t <= mid:
            break
        else:
            wood += t-mid
    if wood > m:
        answer = mid
        binary_search(mid+1, e)

    elif wood < m:
        binary_search(s, mid-1)

    elif wood == m:
        answer = mid
        return


binary_search(0, max_h)
print(answer)
