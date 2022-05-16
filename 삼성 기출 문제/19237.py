# https://www.acmicpc.net/problem/19237

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] > 0:
            graph[i][j] = [temp[j], K]
        else:
            graph[i][j] = [temp[j], 0]
shark_directions = list(map(int, input().split()))
shark_info = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
shark_cur_position = []

# graph에는 숫자(상어 번호) 또는 [상어번호, 가스 수] 가 들어간다.

# 방향
dx = [None, -1, 1, 0, 0]
dy = [None, 0, 0, -1, 1]


def find_cur_sharks():
    shark_cur_position = [[] for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] != 0 and graph[i][j][1] == K:
                shark_cur_position[graph[i][j][0] - 1] = [i, j]

    return shark_cur_position


def find_smell(num):
    smell_of_num = []
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == num + 1 and graph[i][j][1] < K:
                smell_of_num.append([i, j])

    return smell_of_num


def reduce_smell():
    for i in range(N):
        for j in range(N):
            if shark_cur_position[graph[i][j][0] - 1] != [i, j]:
                graph[i][j][1] -= 1
            if graph[i][j][1] <= 0:
                graph[i][j] = [0, 0]


def move_shark():
    for num, position in enumerate(shark_cur_position):
        if position is None:
            continue

        x, y = position
        # 현재 보는 방향
        cur_direction = shark_directions[num] - 1

        nx, ny = x, y
        flag = 0
        # 보는 방향과 우선순위 기반 다음 방향 정하기
        # 1. 가스가 없는 칸 BFS-DFS (여기서 다른 상어의 위치일 때는 포함시킴. 동시에 움직이기 때문)
        for priority in range(4):
            next_direction = shark_info[num][cur_direction][priority]
            nx, ny = x + dx[next_direction], y + dy[next_direction]

            if not (0 <= nx < N and 0 <= ny < N) or 0 < graph[nx][ny][1] < K:
                flag += 1
                continue

            shark_directions[num] = next_direction
            break

        # 2. 만약 주변에 빈 칸이 없다면 내 가스로 이동
        if flag == 4:
            for priority in range(4):
                next_direction = shark_info[num][cur_direction][priority]
                nx, ny = x + dx[next_direction], y + dy[next_direction]

                if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny][0] != num + 1:
                    continue

                shark_directions[num] = next_direction
                break

        # 다음 이동할 칸에 이미 나보다 큰 상어가 자리잡고 있으면 사라짐. (=None)
        if [nx, ny] in shark_cur_position[:num]:
            shark_cur_position[num] = None
        else:
            shark_cur_position[num] = [nx, ny]

    # print(shark_cur_position)
    for num, position in enumerate(shark_cur_position):
        if position is None:
            continue
        x, y = position
        graph[x][y] = [num + 1, K]


def check_graph():
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] > 1 and graph[i][j][1] == K:
                return True
    return False


if __name__ == '__main__':
    cnt = 0
    shark_cur_position = find_cur_sharks()

    while check_graph() and cnt <= 1000:
        move_shark()
        reduce_smell()
        cnt += 1

    print(-1 if cnt > 1000 else cnt)
