# https://www.acmicpc.net/problem/17425

T = int(input())
dp = [0] * 1000001

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        dp[j] += i
    dp[i] += dp[i - 1]

for _ in range(T):
    N = int(input())
    print(dp[N])
