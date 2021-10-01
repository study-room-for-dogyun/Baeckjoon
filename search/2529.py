# https://www.acmicpc.net/problem/2529

k = int(input())
sign = list(map(str, input().split()))

maxi = [0]
mini = [100]

def dfs_max(depth, route, used):
    global maxi, mini

    if depth == k:
        if sum(route) > sum(maxi):
            maxi = route[:]
        return

    for i in range(9, -1, -1):
        if used[i]:
            continue

        if sign[depth] == '<':
            if route[-1] < i:
                used[i] = True
                dfs_max(depth+1, route+[i], used)
                used[i] = False

        else:
            if route[-1] > i:
                used[i] = True
                dfs_max(depth+1, route+[i], used)
                used[i] = False

def dfs_min(depth, route, used):
    global maxi, mini

    if depth == k:
        if sum(route) < sum(mini):
            mini = route[:]
        return

    for i in range(10):
        if used[i]:
            continue

        if sign[depth] == '<':
            if route[-1] < i:
                used[i] = True
                dfs_min(depth+1, route+[i], used)
                used[i] = False

        else:
            if route[-1] > i:
                used[i] = True
                dfs_min(depth+1, route+[i], used)
                used[i] = False

used = [False] * 10
for i in range(9, -1, -1):
    used[i] = True
    dfs_max(0, [i], used)
    used[i] = False

for i in range(10):
    used[i] = True
    dfs_min(0, [i], used)
    used[i] = False

print("".join(map(str, maxi)))
print("".join(map(str, mini)))