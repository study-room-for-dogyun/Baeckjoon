import copy

graph = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [temp[2 * j], temp[2 * j + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def can_eat(array, x, y):  # 상어가 먹을 수 있는 후보 위치 반환
    positions = []
    direction = array[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions


def find_fish(array, num):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == num:
                return [i, j]
    return None


def move_fish(array, now_x, now_y):  # 물고기 이동
    position = []
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        d = array[x][y][1]  # 방향

        while True:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y):  # 공간의 경계, 상어 있는 칸 확인
                    # 값 교체
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], d
                    break
            d = (d + 1) % 8


def dfs(array, x, y, total):
    global ans
    array = copy.deepcopy(array)

    # 해당 위치 물고기 먹기
    number = array[x][y][0]
    array[x][y][0] = -1

    # 물고기 이동
    move_fish(array, x, y)

    # 상어 이동할 수 있는 후보 확인
    result = can_eat(array, x, y)

    ans = max(ans, total + number)
    for next_x, next_y in result:
        dfs(array, next_x, next_y, total + number)


ans = 0
dfs(graph, 0, 0, 0)
print(ans)
