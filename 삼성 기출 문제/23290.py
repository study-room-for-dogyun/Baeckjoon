# https://www.acmicpc.net/problem/23290
from itertools import product
from collections import deque

M, S = map(int, input().split())
fish_map = [[deque() for _ in range(4)] for _ in range(4)]
egg_map = [[deque() for _ in range(4)] for _ in range(4)]
smell_map = [[deque() for _ in range(4)] for _ in range(4)]

# Init
for _ in range(M):
    i, j, d = map(int, input().split())
    fish_map[i - 1][j - 1].append(d - 1)
shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dsx = [-1, 0, 1, 0]
dsy = [0, -1, 0, 1]


def find_fish_and_add_smell():
    result = []
    for i in range(4):
        for j in range(4):
            for k in range(len(smell_map[i][j])):
                smell_map[i][j][k] += 1
            for d in fish_map[i][j]:
                result.append([i, j, d])
    return result


def move_fish():
    for x, y, d in find_fish_and_add_smell():
        # 자기 자리에 알 생성
        egg_map[x][y].append(d)
        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < 4 and 0 <= ny < 4) or [nx, ny] == [shark_x, shark_y] or smell_map[nx][ny]:
                d = (d - 1) % 8
                continue

            fish_map[nx][ny].append(d)
            fish_map[x][y].popleft()
            break


def move_shark():
    global shark_x, shark_y

    # 루트 찾기
    route = []
    sub_route = []
    eat_cnt = 0

    for direction in product(range(4), range(4), range(4)):
        visited = [[False] * 4 for _ in range(4)]
        x, y = shark_x, shark_y

        eat_cnt_in_this_direction = 0
        is_moved_three_direction = True

        for d in direction:
            nx, ny = x + dsx[d], y + dsy[d]
            if not (0 <= nx < 4 and 0 <= ny < 4):
                is_moved_three_direction = False
                break

            if not visited[nx][ny]:
                eat_cnt_in_this_direction += len(fish_map[nx][ny])
                visited[nx][ny] = True
            x, y = nx, ny

        if eat_cnt_in_this_direction < eat_cnt or not is_moved_three_direction:
            continue

        if not sub_route:
            sub_route = direction
        if eat_cnt < eat_cnt_in_this_direction:
            eat_cnt = eat_cnt_in_this_direction
            route = direction

    if not route:
        route = sub_route

    # 먹으면서 이동하기
    for d in route:
        nx, ny = shark_x + dsx[d], shark_y + dsy[d]
        if fish_map[nx][ny]:
            smell_map[nx][ny].append(0)
            fish_map[nx][ny] = deque()
        shark_x, shark_y = nx, ny


def remove_and_copy():
    for i in range(4):
        for j in range(4):
            fish_map[i][j] += egg_map[i][j]
            egg_map[i][j] = deque()
            while smell_map[i][j] and smell_map[i][j][0] == 2:
                smell_map[i][j].popleft()


for _ in range(S):
    move_fish()
    move_shark()
    remove_and_copy()

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(fish_map[i][j])
print(ans)
