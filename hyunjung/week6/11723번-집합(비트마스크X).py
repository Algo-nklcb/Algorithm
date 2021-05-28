import sys

m = int(sys.stdin.readline())
S = set()
for _ in range(m):
    cmd = sys.stdin.readline()

    if cmd == "all\n":
        S = {i for i in range(1, 21)}

    elif cmd == "empty\n":
        S = set()
    else:
        cmd, x = cmd.split(' ')
        x = int(x)
        if cmd == "add":
            S.add(x)
        elif cmd == "check":
            print(int(x in S))
        elif cmd == "remove":
            S.discard(x)
        elif cmd == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
