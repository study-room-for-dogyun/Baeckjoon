# https://www.acmicpc.net/problem/13913

from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001
move = [0] * 100001


def path(x):
    arr = []
    temp = x
    for _ in range(dp[x] + 1):
        arr.append(temp)
        temp = move[temp]

    print(' '.join(map(str, arr[::-1])))


def bfs():
    q = deque([N])

    while q:
        cur = q.popleft()

        if cur == K:
            print(dp[cur])
            path(cur)
            return

        for i in (cur + 1, cur - 1, 2 * cur):
            if 0 <= i < 100001 and dp[i] == 0:
                q.append(i)
                dp[i] = dp[cur] + 1
                move[i] = cur


bfs()
