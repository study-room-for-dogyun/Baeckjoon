# https://www.acmicpc.net/problem/17837

N, K = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]
hourse = [list(map(int, input().split())) for _ in range(K)]
field = [[[] for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def init():
    for num, h in enumerate(hourse):
        x, y, d = h
        field[x - 1][y - 1].append(num)
        for i in range(3):
            hourse[num][i] -= 1


def is_end():
    for x, y, d in hourse:
        if len(field[x][y]) >= 4:
            return True
    return False


def turn():
    for num, info in enumerate(hourse):
        x, y, d = info
        order = field[x][y].index(num)
        nx, ny = x + dx[d], y + dy[d]

        # 갈려는 방향이 막혔거나 파란색이면? 방향 반대로 바꾸기
        if not (0 <= nx < N and 0 <= ny < N) or place[nx][ny] == 2:
            d = d + 1 if d % 2 == 0 else d - 1
            hourse[num][2] = d
            nx, ny = x + dx[d], y + dy[d]

        # 파란색이거나 막혀있으면? 가만히 있기
        if not (0 <= nx < N and 0 <= ny < N) or place[nx][ny] == 2:
            continue

        # 갈려는 쪽이 하얀색이면?
        elif place[nx][ny] == 0:
            field[nx][ny] += field[x][y][order:]

        # 갈려는 쪽이 빨간색이면?
        elif place[nx][ny] == 1:
            field[nx][ny] += reversed(field[x][y][order:])

        field[x][y] = field[x][y][:order]

        for k in field[nx][ny]:
            hourse[k][0] = nx
            hourse[k][1] = ny

        if is_end():
            return False

    return True


init()

ans = 1
while turn() and ans <= 1000:
    ans += 1

print(ans if ans <= 1000 else -1)
