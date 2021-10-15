# https://www.acmicpc.net/problem/17140

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]


def oper():
    global arr

    longest = 0
    for idx, row in enumerate(arr):
        cnt = {}
        for i in row:
            if i == 0:
                continue
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        temp = sorted(cnt.items())
        temp.sort(key=lambda x: x[1])

        new = []
        for a, b in temp:
            new.append(a)
            new.append(b)

        if len(new) > 100:
            arr[idx] = new[:100]
            longest = 100
        else:
            arr[idx] = new
            longest = max(longest, len(new))

    for idx, row in enumerate(arr):
        if len(row) != longest:
            arr[idx] += [0] * (longest - len(row))


ans = -1
for i in range(101):
    len_r = len(arr)
    len_c = len(arr[0])

    if len_r > r-1 and len_c > c-1:
        if arr[r-1][c-1] == k:
            ans = i
            break

    if len_r >= len_c:
        oper()
    else:
        arr = list(map(list, zip(*arr)))
        oper()
        arr = list(map(list, zip(*arr)))

print(ans)
