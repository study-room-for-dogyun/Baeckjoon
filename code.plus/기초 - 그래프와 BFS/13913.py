# https://www.acmicpc.net/problem/13913

from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001

q = deque([N])
while q:
    cur = q.popleft()

    if cur + 1 < 100001:
        if dp[cur + 1] == 0 or dp[cur + 1] > dp[cur] + 1:
            q.append(cur + 1)
            dp[cur + 1] = dp[cur] + 1
    if cur - 1 > 0:
        if dp[cur - 1] == 0 or dp[cur - 1] > dp[cur] + 1:
            q.append(cur - 1)
            dp[cur - 1] = dp[cur] + 1
    if 2 * cur < 100001:
        if dp[2 * cur] == 0 or dp[2 * cur] > dp[cur] + 1:
            q.append(2 * cur)
            dp[2 * cur] = dp[cur] + 1

print(dp[17])
