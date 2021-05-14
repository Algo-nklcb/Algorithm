from sys import stdin
n = int(stdin.readline())

answer = []
def pickNumber():
    for num in range(10):
        if num in answer:
            continue
        answer.append(num)

