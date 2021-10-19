# https://www.acmicpc.net/problem/14499

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

#       동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def right():
    temp = dice[3][1]
    dice[3][1] = dice[1][2]
    dice[1][2] = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] = temp

def left():
    temp = dice[3][1]
    dice[3][1] = dice[1][0]
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] = temp

def up():
    temp = dice[0][1]
    for i in range(3):
        dice[i][1] = dice[i+1][1]
    dice[-1][1] = temp

def down():
    temp = dice[-1][1]
    for i in range(3, 0, -1):
        dice[i][1] = dice[i-1][1]
    dice[0][1] = temp

for c in command:

    nx, ny = x+dx[c], y+dy[c]
    if not(0 <= nx < N and 0 <= ny < M):
        continue

    if c == 1:
        right()
    elif c == 2:
        left()
    elif c == 3:
        up()
    else:
        down()

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[3][1]
    else:
        dice[3][1] = graph[nx][ny]
        graph[nx][ny] = 0
    
    print(dice[1][1])
    x, y = nx, ny

    # 윗면+아래면 = 7
    # 위쪽으로 굴리면 중간에꺼만 위로 한 칸씩
    # 오른쪽으로 굴리면 중간에꺼랑 맨 밑에꺼 굴림
    # 왼쪽으로 굴리면 중간에꺼랑 맨 밑에꺼 굴림.
    # 윗 면 = [1][1]
    # 아랫 면 = [3][1]
    # 깊은 복사 문제때문에 안 되는거 같은데 -> 아닌듯