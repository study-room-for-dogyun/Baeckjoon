# https://www.acmicpc.net/problem/21608

N = int(input())
stdinfo = [list(map(int, input().split())) for _ in range(N ** 2)]
graph = [[0] * N for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def set_sit(num, likes):
    # 스코어링
    highest = 0
    highests_sit = []
    score = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                continue
            x, y = i, j
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if graph[nx][ny] in likes:
                    score[x][y] += 1

            if score[x][y] > highest:
                highest = score[x][y]
                highests_sit = [[x, y]]
            elif score[x][y] == highest:
                highests_sit.append([x, y])

    if len(highests_sit) == 1:
        x, y = highests_sit[0]
        graph[x][y] = num
        return

    # 스코어가 여러 개라면 비어있는 칸으로 세기
    empty_score = []
    highest_empty_score = 0
    for x, y in highests_sit:  # highests_sit은 이미 3번 조건을 만족하여 정렬되어있음.
        temp = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if graph[nx][ny] == 0:
                temp += 1

        if temp > highest_empty_score:
            highest_empty_score = temp
            empty_score = [[x, y]]
        elif temp == highest_empty_score:
            empty_score.append([x, y])

    x, y = empty_score[0]
    graph[x][y] = num


def count(x, y, num):
    likes = []
    for i in stdinfo:
        if i[0] == num:
            likes = i[1:]
            break

    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if graph[nx][ny] in likes:
            cnt += 1

    if cnt == 0:
        return 0
    return 10 ** (cnt - 1)


ans = 0
for info in stdinfo:
    set_sit(info[0], info[1:])

for i in range(N):
    for j in range(N):
        ans += count(i, j, graph[i][j])

print(ans)
