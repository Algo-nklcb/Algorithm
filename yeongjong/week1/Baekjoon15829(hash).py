def hash(p: str) -> int:
    h = 0
    for i, char in enumerate(p):
        h += (ord(char) - 96) * (31 ** i)
        h %= 1234567891
    return h

input().split(' ')
string = input()
print(hash(string))