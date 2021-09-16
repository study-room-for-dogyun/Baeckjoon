# https://www.acmicpc.net/problem/15666

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

def dfs(value, depth):

    if depth == m:
        print(" ".join(list(map(str, value))))
        return
    value = list(value)

    for i in nums:
        if int(value[-1]) <= i:
            value.append(i)
            dfs(value, depth+1)
            value.pop()

for i in nums:
    dfs([i], 1)