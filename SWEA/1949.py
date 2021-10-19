# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
answers = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(length, x, y, dig):
    global ans
    ans = max(length, ans)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
            continue

        if graph[x][y] > graph[nx][ny]:
            visited[nx][ny] = True
            dfs(length + 1, nx, ny, dig)
            visited[nx][ny] = False
        else:
            if dig and abs(graph[nx][ny] - graph[x][y]) < K:
                temp = graph[nx][ny]
                graph[nx][ny] = graph[x][y] - 1
                visited[nx][ny] = True

                dfs(length + 1, nx, ny, 0)

                graph[nx][ny] = temp
                visited[nx][ny] = False


for _ in range(T):

    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # find highest
    highest = 0
    for i in graph:
        highest = max(highest, max(i))

    start = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == highest:
                start.append([i, j])

    ans = 0
    for x, y in start:
        visited[x][y] = True
        dfs(1, x, y, 1)
        visited[x][y] = False

    answers.append(ans)

for idx, i in enumerate(answers):
    print(f'#{idx + 1} {i}')
