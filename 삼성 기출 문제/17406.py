# https://www.acmicpc.net/problem/17406

from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
rotate_info = [list(map(int, input().split())) for _ in range(K)]


def counting(graph):
    result = 10e9
    for i in graph:
        result = min(result, sum(i))
    return result


def rotate(graph, order):

    for r, c, s in order:
        arr = []
        for i in range(r - s - 1, r + s):
            arr.append(graph[i][c - s - 1:c + s])

        for size in range(s):
            temp = arr[size][size]
            for i in range(size, 2 * s - size):
                arr[i][size] = arr[i + 1][size]

            for i in range(size, 2 * s - size):
                arr[-size - 1][i] = arr[-size - 1][i + 1]

            for i in range(size + 1, 2 * s - size + 1):
                arr[-i][-size - 1] = arr[-i - 1][-size - 1]

            for i in range(size + 1, 2 * s - size):
                arr[size][-i] = arr[size][-i - 1]
            arr[size][size + 1] = temp

        k = 0
        for i in range(r - s - 1, r + s):
            graph[i][c - s - 1:c + s] = arr[k]
            k += 1

    return counting(graph)


ans = 10e9

for i in permutations(rotate_info, K):
    new_arr = deepcopy(A)
    ans = min(ans, rotate(new_arr, i))

print(ans)
