# https://www.acmicpc.net/problem/14226
from collections import deque

s = int(input())

time = [[-1] * 1001 for _ in range(1001)]

q = deque([[1, 0]])
time[1][0] = 0

while q:
    cur, clip = q.popleft()

    if cur == s:
        print(time[cur][clip])
        break


    # 복사
    if time[cur][cur] == -1:
        time[cur][cur] = time[cur][clip] + 1
        q.append([cur, cur])

    # 붙여넣기
    if cur+clip < 1001 and time[cur+clip][clip] == -1:
        time[cur+clip][clip] = time[cur][clip] + 1
        q.append([cur+clip, clip])

    # 지우기
    if 2 <= cur-1 and time[cur-1][clip] == -1:
        time[cur-1][clip] = time[cur][clip] + 1
        q.append([cur-1, clip])