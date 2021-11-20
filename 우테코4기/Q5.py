# 문제 설명
# rows행 columns열로 이루어진 격자가 있습니다. 처음에 모든 격자 칸 안에는 숫자 0이 쓰여 있습니다. 당신은 다음과 같은 과정을 통하여 격자에 숫자들을 채우고자 합니다.
#
# 현재 위치를 1행 1열로 정하고, 그 위치에 숫자 1을 씁니다.
# r을 현재 위치의 행, c를 현재 위치의 열로 정의합니다.
# 만약 격자 내에 0이 쓰인 칸이 없거나, 더 이상 0이 쓰여 있는 칸에 다른 숫자를 쓸 수 없게 된다면 과정을 즉시 종료합니다.
# 만약 가장 최근에 쓴 숫자가 짝수라면, r행 c열에서 r+1행 c열로 이동합니다. r = rows라면, 1행으로 이동합니다.
# 만약 가장 최근에 쓴 숫자가 홀수라면, r행 c열에서 r행 c+1열로 이동합니다. c = columns라면, 1열로 이동합니다.
# 도착한 칸에 원래 쓰여 있던 수를 지우고 가장 최근에 쓴 숫자 + 1을 씁니다.
# 2번 과정으로 돌아갑니다.
# 정수 rows와 columns가 매개변수로 주어집니다. 주어진 과정을 따라 rows행 columns열로 이루어진 격자에 숫자를 썼을 때, 해당 격자를 2차원 정수 배열로 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 2 ≤ rows ≤ 1,000
# 2 ≤ columns ≤ 1,000
# 입출력 예
# rows	columns	result
# 3	4	[[8,2,13,14],[16,10,4,15],[17,11,12,6]]
# 3	3	[[1,2,0],[0,3,4],[6,0,5]]

from copy import deepcopy

def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)]

    def zcheck():
        for i in range(rows):
            if 0 in graph[i]:
                return True
        return False

    x, y = 0, 0
    graph[x][y] = 1
    nx, ny = x, y

    prev_route = [[0, 0]]
    cur_route = [[0, 0]]

    # 처음 경로
    while True:
        if not zcheck():
            break
        if graph[x][y] % 2 == 0:
            nx = (x + 1) % rows
            ny = y
        else:
            nx = x
            ny = (y + 1) % columns

        if [nx, ny] == [0, 0]:
            break

        graph[nx][ny] = graph[x][y] + 1
        x, y = nx, ny
        prev_route.append([x, y])

    prev_map = deepcopy(graph)

    while True:
        if not zcheck():
            break

        if graph[x][y] % 2 == 0:
            nx = (x + 1) % rows
            ny = y
        else:
            nx = x
            ny = (y + 1) % columns

        if [nx, ny] == [0, 0]:
            if prev_route == cur_route:
                return prev_map

            prev_route = cur_route[:]
            cur_route = []

        graph[nx][ny] = graph[x][y] + 1
        x, y = nx, ny
        cur_route.append([x, y])

    return graph