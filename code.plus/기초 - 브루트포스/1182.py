# https://www.acmicpc.net/problem/1182

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
def dfs(value, idx, depth):
    global answer

    if value == s:
        answer += 1

    if idx == n-1:
        return
    
    for next in range(idx+1, n):
        dfs(value+nums[next], next, depth+1)

for i in range(n):
    dfs(nums[i], i, 0)

print(answer)