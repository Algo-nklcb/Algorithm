t = int(input())

for _ in range(t):
    n = int(input())
    tmp = []
    for _ in range(n):
        tmp.append(int(input()))
    tmp.sort()
    tels = list(map(str, tmp))
    isConsistency = "YES"
    for i in range(n):
        if isConsistency == "NO":
            break
        for j in range(i+1, n):
            if isConsistency == "NO":
                break
            cnt = 0
            for k in range(len(tels[i])):
                if tels[i][k] == tels[j][k]:
                    cnt += 1
                if cnt == len(tels[i]):
                    isConsistency = "NO"
                    break
    print(isConsistency)
