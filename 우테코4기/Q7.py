# 문제 설명
# 한 변의 길이가 1인 정삼각형 n2 개로 구성된 정삼각형 격자가 있습니다. 격자의 각 칸에는 문자(영어 대소문자 또는 숫자) 하나가 쓰여 있습니다. 당신은 이 격자를 시계 방향 또는 반시계 방향으로 120도 회전하고자 합니다.
#
# 격자의 정보를 나타내는 문자열 배열 grid와 회전 방향을 나타내는 clockwise가 매개변수로 주어집니다. 주어진 격자를 clockwise가 의미하는 방향으로 회전시킨 결과를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ grid의 길이 ≤ 1,000
# grid[i]의 길이 = 2 * i + 1
# grid[i]는 영어 대소문자 또는 숫자로 이루어진 문자열입니다.
# clockwise가 참이면 시계 방향, 거짓이면 반시계 방향으로 120도 회전해야 함을 의미합니다.
# 입출력 예
# grid	clockwise	result
# ["1","234","56789"]	true	["5","762","98431"]
# ["A","MAN","DRINK","WATER11"]	false	["1","K1R","NNIET","AAMRDAW"]

def rotate(graph):
    height = len(graph)
    new = []
    for h in range(height):
        cur = height - 1
        temp = []
        for k in range(2 * h, -1, -1):
            if k % 2 == 0 and k != 2 * h:
                cur -= 1
            temp.append(graph[cur][k])
        new.append(temp)
    return new


def solution(grid, clockwise):
    answer = []
    for i in grid:
        answer.append(list(map(str, i)))

    answer = rotate(answer)
    if not clockwise:
        answer = rotate(answer)

    for idx, i in enumerate(answer):
        answer[idx] = "".join(i)

    return answer