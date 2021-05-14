from sys import stdin
from collections import deque, defaultdict

n = int(stdin.readline())


# build_times = [0] * (n + 1) # dp 용
# build_times[0] = -1
# info_buildings = [-1] # 시간, 필요 건물 ... , -1

# for _ in range(1, n + 1):
#     info_buildings.append(list(map(int, stdin.readline().split())))


# def calcTime(neededTime, neededBuilding) -> int:
#     costructionTimes = []
#     if len(neededBuilding) == 0:
#         return max(costructionTimes) + neededTime
#     for neededBuildingNum in neededBuilding:
#         if build_times[neededBuildingNum] != 0:
#             costructionTimes.append(build_times[neededBuildingNum])
#             continue
#         costructionTimes.append(calcTime(info_buildings[neededBuildingNum][0], info_buildings[neededBuildingNum][1:-1]))
#     return max(costructionTimes) + neededTime

#     # for i in range(info_buildings[buildingNum]):
#     #     if i == -1:
#     #         build_time[buildingNum] = time
#     #         time = 0
#     #         return
#     #     if i == 0:
#     #         time += info_buildings[buildingNum][i]
#     #         continue
#     #     if build_time[i] != 0:
#     #         time += build_time[i]
#     #         continue
#     #     calcTime(info_buildings[buildingNum][i])

# for buildingNum, info_building in enumerate(info_buildings):
#     if buildingNum == 0:
#         continue
#     neededBuilding = info_building[1:-1]
#     neededTime = info_building[0]
#     # while 0 in build_times:
#     temp = 0
#     while temp < 5:
#         build_times[buildingNum] = calcTime(neededTime, neededBuilding)
#         temp += 1

# print(build_times)












buildingsIndegrees = [0] * (n + 1)
buildingsIndegrees[0] = -1
buildingsTime = [0] * (n + 1)
buildingsTime[0] = -1

dp = [[] for _ in range(n + 1)]
graph = defaultdict(list)

for i in range(1, n + 1):
    info_building = list(map(int, stdin.readline().split()))
    buildingsTime[i] = info_building[0]
    neededBuildings = info_building[1:-1]
    buildingsIndegrees[i] = len(neededBuildings)

    if len(neededBuildings) == 0:
        dp[i] = buildingsTime[i]

    for neededBuilding in neededBuildings:
        graph[neededBuilding].append(i)

que = deque()

for buildingNum, indegree in enumerate(buildingsIndegrees):

    if indegree == 0:
        que.append(buildingNum)

while que:
    buildingNum = que.popleft()

    for nextBuildingNum in graph[buildingNum]:
        buildingsIndegrees[nextBuildingNum] -= 1
        dp[nextBuildingNum].append(buildingsTime[nextBuildingNum])
        if buildingsIndegrees[nextBuildingNum] == 0:
            que.append(nextBuildingNum)
            dp[nextBuildingNum] = max(dp[nextBuildingNum]) + buildingsTime[nextBuildingNum]
