n = int(input())
image = [0 for _ in range(n)]
for i in range(n):
    image[i] = list(map(int, input()))


def recursive(s_i, s_j, k):  # start i, start j
    is_all_1 = True
    is_all_0 = True
    for i in range(s_i, s_i+k):
        for j in range(s_j, s_j+k):
            if image[i][j] == 0:
                is_all_1 = False
            else:
                is_all_0 = False

    if is_all_1:
        print(1, end='')
        return
    elif is_all_0:
        print(0, end='')
        return
    else:
        print('(', end='')
        recursive(s_i, s_j, k//2)
        recursive(s_i, s_j+(k//2), k//2)
        recursive(s_i+(k//2), s_j, k//2)
        recursive(s_i+(k//2), s_j+(k//2), k//2)
        print(')', end='')


recursive(0, 0, n)
