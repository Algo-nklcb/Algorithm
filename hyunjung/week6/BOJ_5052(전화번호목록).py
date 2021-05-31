import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head
        curr.cnt += 1

        for c in string:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.cnt += 1

    def count(self, prefix):
        curr = self.head

        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]

        return curr.cnt


t = int(input())

for _ in range(t):
    n = int(input())
    tels = []
    for _ in range(n):
        tels.append(input())
    tries = Trie()

    for tel in tels:
        tries.insert(tel)
    isConsitency = "YES"
    for tel in tels:
        if tries.count(tel) > 1:
            isConsitency = "NO"
            break
    print(isConsitency)
