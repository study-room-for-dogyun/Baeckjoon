# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 10987654321


def distance(x, y, chicken):
    min_d = 10987654321
    for i, j in chicken:
        min_d = min(min_d, abs(x-i)+abs(y-j))
    return min_d


# 치킨, 집 위치
house = []
chicken = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            house.append([x, y])
        if graph[x][y] == 2:
            chicken.append([x, y])


for positions in combinations(chicken, M):
    temp = 0
    for x, y in house:
        temp += distance(x, y, positions)
    ans = min(temp, ans)

print(ans)