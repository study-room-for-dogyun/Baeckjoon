# https://www.acmicpc.net/problem/16235
from collections import deque

N, M, K = map(int, input().split())
S2D2 = [list(map(int, input().split())) for _ in range(N)]
energy = [[5] * N for _ in range(N)]

tree_info = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    tree_info[x - 1][y - 1].append(age)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 양분 먹기 및 죽기
    for i in range(N):
        for j in range(N):
            tree_info[i][j].sort()
            for idx, tree_age in enumerate(tree_info[i][j]):
                if tree_age <= energy[i][j]:
                    energy[i][j] -= tree_age
                    tree_info[i][j][idx] += 1
                else:  # 현재 인덱스부터 나무는 죽어서 양분으로 돌아감.
                    for die in tree_info[i][j][idx:]:
                        energy[i][j] += die // 2        # 한꺼번에 sum 하면 안 됨.
                    tree_info[i][j] = tree_info[i][j][:idx]
                    break

    # 번식하기
    for i in range(N):
        for j in range(N):
            for tree_age in tree_info[i][j]:
                if tree_age % 5 == 0:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if not (0 <= nx < N and 0 <= ny < N):
                            continue
                        tree_info[nx][ny].append(1)

    # 양분 추가하기
    for i in range(N):
        for j in range(N):
            energy[i][j] += S2D2[i][j]

ans = 0
for row in tree_info:
    for elem in row:
        ans += len(elem)

print(ans)
