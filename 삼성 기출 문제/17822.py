# https://www.acmicpc.net/problem/17822

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def rotate(num, direct, cnt):
    global board

    for _ in range(cnt):
        if direct:  # 반시계방향
            board[num].append(board[num][0])
            board[num] = board[num][1:]
        else:  # 시계방향
            board[num] = [0] + board[num]
            board[num][0] = board[num][-1]
            board[num] = board[num][:M]


def check_adj():
    global board

    is_have_same = False
    same = []
    # 가로 인접
    for num in range(N):
        for i in range(M):
            if board[num][i] == board[num][(i + 1) % M] and board[num][i] != 0:
                same.append([num, i])
                same.append([num, (i + 1) % M])

    # 세로 인접
    for i in range(M):
        for num in range(N - 1):
            if board[num][i] == board[num + 1][i] and board[num][i] != 0:
                same.append([num, i])
                same.append([num + 1, i])

    for i, j in same:
        board[i][j] = 0

    if same:
        return True
    return False


def total_board():
    total = 0
    for i in board:
        total += sum(i)
    return total


def mean_board():
    non_zero_cnt = 0
    for i in board:
        non_zero_cnt += M - i.count(0)

    if non_zero_cnt == 0:
        return 0
    return total_board() / non_zero_cnt


def replace_num():
    global board

    mean = mean_board()
    for num in range(N):
        for i in range(M):
            if board[num][i] == 0:
                continue

            if board[num][i] > mean:
                board[num][i] -= 1
            elif board[num][i] < mean:
                board[num][i] += 1


for _ in range(T):
    x, d, k = map(int, input().split())

    for i in range(x, N + 1, x):
        rotate(i - 1, d, k)

    if not check_adj():
        replace_num()

print(total_board())
