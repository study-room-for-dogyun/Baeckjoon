# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&categoryId=AV4suNtaXFEDFAUf&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

from collections import deque

T = int(input())
answers = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(q):
    global ans, max_on_cnt

    # 모든 셀 다 연결시도 해봤다면.
    if not q:
        line_cnt = 0
        for i in graph:  # 전선 개수
            line_cnt += i.count(2)

        on_cnt = 0
        for i in on:  # 켜져있는 개수
            on_cnt += i.count(True)

        if on_cnt >= max_on_cnt:
            max_on_cnt = on_cnt
            ans = min(ans, line_cnt)

        return

    ix, iy = q.popleft()
    x, y = ix, iy
    for i in range(4):

        # 해당 방향으로 쭉 연결될 수 있는지 체크
        check = True
        while True:
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                break

            if graph[nx][ny] != 0:
                check = False
                break

            x, y = nx, ny

        # 해당 방향으로 연결이 가능하다면 연결하기
        if check:
            x, y = ix, iy
            while True:
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < N and 0 <= ny < N):
                    break
                graph[nx][ny] = 2
                x, y = nx, ny

            on[ix][iy] = True

            dfs(q)

            x, y = ix, iy
            while True:
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < N and 0 <= ny < N):
                    break
                graph[nx][ny] = 0
                x, y = nx, ny

            on[ix][iy] = False


for _ in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    on = [[False] * N for _ in range(N)]

    cell = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and 0 < i < N - 1 and 0 < j < N - 1:
                cell.append([i, j])
            if graph[i][j] == 1 and i == 0 or i == N - 1 or j == 0 or j == N - 1:
                on[i][j] = True

    max_on_cnt = 0
    ans = 10e9
    dfs(cell)

    answers.append(ans)

for idx, i in enumerate(answers):
    print(f'#{idx + 1} {i}')
