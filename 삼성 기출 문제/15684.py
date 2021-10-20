# https://www.acmicpc.net/problem/15684

N, M, H = map(int, input().split())
bridge = [[False] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    bridge[a - 1][b - 1] = True


def check():
    for start in range(N):
        k = start
        for i in range(H):
            if bridge[i][k]:
                k += 1
            elif 0 < k and bridge[i][k - 1]:
                k -= 1
        if start != k:
            return False
    return True


def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return

    if cnt == 3 or ans < cnt:
        return

    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N - 1):
            if not bridge[i][j] and not bridge[i][j + 1]:
                bridge[i][j] = True
                dfs(cnt + 1, i, j + 2)
                bridge[i][j] = False


ans = 4

dfs(0, 0, 0)

print(ans if ans < 4 else -1)
