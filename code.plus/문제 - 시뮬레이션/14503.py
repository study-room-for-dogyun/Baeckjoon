# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

# 0: 청소 안 한 공간
# 1: 벽
# 2: 청소 한 공간
# 현재 방향 d 기준 -1 왼쪽, +2하면 뒤쪽임.
# 방향 바꿀 때 : d 값 수정
# 이동만 할 때 : r, c 값에 d값 더해서 수정
# 그러니까 후진 할 때는 d값은 업데이트 하면 안 됨.
while True:

    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1

    check = 0
    for _ in range(4):
        d -= 1
        next_position = graph[r + dx[d%4]][c + dy[d%4]]
        if next_position == 0:
            r += dx[d%4]
            c += dy[d%4]
            break
        check += 1
    
    if check == 4:
        back_position = graph[r + dx[(d+2)%4]][c + dy[(d+2)%4]]
        if back_position == 1:
            break
        else:
            r += dx[(d+2)%4]
            c += dy[(d+2)%4]

print(answer)