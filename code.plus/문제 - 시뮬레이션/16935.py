# https://www.acmicpc.net/problem/16935

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
oper = list(map(int, input().split()))


def one():
    global arr
    temp = []
    for i in arr:
        temp.append(i)
    for i in range(len(arr)):
        arr[i] = temp[-(i + 1)]


def two():
    global arr
    arr = list(map(list, zip(*arr)))
    one()
    arr = list(map(list, zip(*arr)))


def three():
    global arr
    arr = list(map(list, zip(*arr[::-1])))


def four():
    global arr
    arr = list(map(list, zip(*arr)))[::-1]


def five():
    # 1: 0 ~ N/2, 0 ~ M/2
    # 2: 0 ~ N/2, M/2 ~ M
    # 3: N/2 ~ N, M/2 ~ M
    # 4: N/2 ~ N, 0 ~ M/2
    temp = []
    for i in range(0, len(arr) // 2):
        temp.append(arr[i][0:len(arr[0]) // 2])

    # 4 -> 1
    for i in range(len(arr) // 2, len(arr)):
        for j in range(len(arr[0]) // 2):
            arr[i - len(arr) // 2][j] = arr[i][j]

    # 3 -> 4
    for i in range(len(arr) // 2, len(arr)):
        for j in range(len(arr[0]) // 2, len(arr[0])):
            arr[i][j - len(arr[0]) // 2] = arr[i][j]

    # 2 -> 3
    for i in range(len(arr) // 2):
        for j in range(len(arr[0]) // 2, len(arr[0])):
            arr[i + len(arr) // 2][j] = arr[i][j]

    # 1 -> 2
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            arr[i][j + len(arr[0]) // 2] = temp[i][j]


def six():
    temp = []
    for i in range(0, len(arr) // 2):
        temp.append(arr[i][0:len(arr[0]) // 2])

    # 2 -> 1
    for i in range(0, len(arr) // 2):
        for j in range(len(arr[0]) // 2, len(arr[0])):
            arr[i][j - len(arr[0]) // 2] = arr[i][j]

    # 3 -> 2
    for i in range(len(arr) // 2, len(arr)):
        for j in range(len(arr[0]) // 2, len(arr[0])):
            arr[i - len(arr) // 2][j] = arr[i][j]

    # 4 -> 3
    for i in range(len(arr) // 2, len(arr)):
        for j in range(0, len(arr[0]) // 2):
            arr[i][j + len(arr[0]) // 2] = arr[i][j]

    # 1 -> 4
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            arr[i + len(arr) // 2][j] = temp[i][j]


for r in oper:
    if r == 1:
        one()
    elif r == 2:
        two()
    elif r == 3:
        three()
    elif r == 4:
        four()
    elif r == 5:
        five()
    elif r == 6:
        six()

for i in arr:
    print(" ".join(map(str, i)))
