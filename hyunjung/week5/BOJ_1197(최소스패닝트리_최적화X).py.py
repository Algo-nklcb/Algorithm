v, e = map(int, input().split(' '))
edges = []
vertexGroup = [{i} for i in range(v+1)]
for i in range(e):
    v1, v2, w = map(int, input().split(' '))
    edges.append((w, v1, v2))
edges.sort()
mstWeight = 0
mstEdgeNum = 0


def canAdd(v1, v2):
    if findGroupLeader(v1) != findGroupLeader(v2):
        return True
    else:
        return False


def findGroupLeader(v):
    return list(vertexGroup[v])[0]


while mstEdgeNum < v-1 and len(edges) != 0:
    w, v1, v2 = edges.pop(0)
    if canAdd(v1, v2):
        mstWeight += w
        mstEdgeNum += 1
        if v1 < v2:
            vertexGroup[v1] = vertexGroup[v1] | vertexGroup[v2]
            for vg in vertexGroup[v1]:
                vertexGroup[vg] = vertexGroup[v1]
        else:
            vertexGroup[v2] = vertexGroup[v1] | vertexGroup[v2]
            for v in vertexGroup[v2]:
                vertexGroup[vg] = vertexGroup[v2]
print(mstWeight)