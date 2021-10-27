# https://www.acmicpc.net/problem/23288

from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dice = [2, 1, 5, 6, 4, 3]
dice_x, dice_y, dice_d = 0, 0, 1

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move_dice():
    global dice_x, dice_y, dice_d

    nx, ny = dice_x + dx[dice_d], dice_y + dy[dice_d]
    if not (0 <= nx < N and 0 <= ny < M):
        dice_d = (dice_d + 2) % 4

    dice_x += dx[dice_d]
    dice_y += dy[dice_d]

    if dice_d == 0:
        temp = dice[0]
        for i in range(3):
            dice[i] = dice[i + 1]
        dice[3] = temp

    elif dice_d == 1:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = dice[5]
        dice[5] = temp

    elif dice_d == 2:
        temp = dice[3]
        for i in range(3, 0, -1):
            dice[i] = dice[i - 1]
        dice[0] = temp
    else:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = dice[4]
        dice[4] = temp


def check_c(x, y):
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    q = deque([[x, y]])
    result = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or graph[nx][ny] != graph[x][y]:
                continue

            q.append([nx, ny])
            visited[nx][ny] = True
            result += 1

    return result


score = 0

for _ in range(K):

    move_dice()
    A = dice[3]
    B = graph[dice_x][dice_y]
    score += check_c(dice_x, dice_y) * B

    if A > B:
        dice_d = (dice_d + 1) % 4
    elif A < B:
        dice_d = (dice_d - 1) % 4

print(score)
