# https://www.acmicpc.net/problem/14890

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def check(road):
    bridge = [False] * N

    for i in range(N - 1):
        if abs(road[i] - road[i + 1]) > 1:
            return False

        if road[i] == road[i + 1]:
            continue

        if road[i] < road[i + 1]:
            len_same = 0
            for j in range(i, -1, -1):
                if road[i] == road[j]:
                    len_same += 1
                else:
                    break

            if len_same < L:
                return False

            if True in bridge[max(i - L + 1, 0):i + 1]:
                return False

            for j in range(max(i - L + 1, 0), i + 1):
                bridge[j] = True

        else:
            len_same = 0
            for j in range(i + 1, N):
                if road[i + 1] == road[j]:
                    len_same += 1
                else:
                    break

            if len_same < L:
                return False

            if True in bridge[i + 1:min(N, i + 1 + L)]:
                return False

            for j in range(i + 1, min(N, i + 1 + L)):
                bridge[j] = True

    return True


for i in range(N):
    if check(graph[i]):
        ans += 1

graph = list(map(list, zip(*graph)))
for i in range(N):
    if check(graph[i]):
        ans += 1

print(ans)
