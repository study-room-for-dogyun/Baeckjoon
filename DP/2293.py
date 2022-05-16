# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

for i in coin:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
