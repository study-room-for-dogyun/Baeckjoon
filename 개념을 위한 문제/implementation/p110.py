
n = int(input())
plans = input().split()

x, y = 1, 1

#    L  R  U  D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 이하 문장은 실행하지 않고 다음 for 실행

    x, y = nx, ny

print(x, y)