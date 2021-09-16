# https://www.acmicpc.net/problem/15686

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


# 치킨집 위치 확인
chicken = []
for x in range(len(graph)):
    for y in range(len(graph)):
        if graph[x][y] == 2:
            chicken.append([x, y])

# 치킨 거리 구하기
def bfs():
    distance = 0



    return distance

# 치킨 집 랜덤뽑기
def dfs(count, depth):

    if depth == m:
        return count

    