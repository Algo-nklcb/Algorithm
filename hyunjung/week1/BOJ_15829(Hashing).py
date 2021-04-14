l = int(input())
s = input()


def hash_func(s: str):
    answer = 0
    for i, c in enumerate(s):
        answer += (ord(c)-96)*(31**i)
        answer %= 1234567891
    return answer


print(hash_func(s))
