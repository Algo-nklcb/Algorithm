import sys

m = int(sys.stdin.readline())
S = set()
for _ in range(m):
    cmd = sys.stdin.readline()

    if cmd == "all\n":
        S = (1 << 21)-1

    elif cmd == "empty\n":
        S = 0
    else:
        cmd, x = cmd.split(' ')
        x = int(x)
        if cmd == "add":
            S |= 1 << int(x)
        elif cmd == "check":
            if S & (1 << int(x)):
                print(1)
            else:
                print(0)
        elif cmd == "remove":
            S &= ~(1 << int(x))
        elif cmd == "toggle":
            S ^= (1 << int(x))
